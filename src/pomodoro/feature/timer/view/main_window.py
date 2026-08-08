"""Главное окно приложения."""

import tkinter as tk
from tkinter import ttk
from pathlib import Path

from src.pomodoro.feature.timer.viewmodel.timer_view_model import TimerViewModel
from src.pomodoro.feature.timer.view.components.timer_display import TimerDisplay


class MainWindow:
    """Главное окно Pomodoro Timer."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("🍅 Pomodoro Timer")
        self.root.geometry("400x500")
        self.root.minsize(350, 250)

        # Создаем ViewModel
        self.view_model = TimerViewModel(root)
        
        # Устанавливаем колбэки для обновления интерфейса
        self.view_model.set_callbacks(
            on_display_update=self._update_time_display,
            on_status_update=self._update_status_display
        )

        self._set_icon()
        self.center_window()
        self._setup_styles()
        self.create_widgets()
        
        # Показываем начальное состояние
        self._update_initial_state()

    def _set_icon(self):
        """Устанавливает иконку окна, если файл существует."""
        icon_path = Path(__file__).parent.parent.parent.parent / "assets" / "icons" / "tomato.png"
        if icon_path.exists():
            try:
                self.root.iconphoto(False, tk.PhotoImage(file=str(icon_path)))
            except Exception:
                pass

    def center_window(self):
        """Центрирует окно на экране."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def _setup_styles(self):
        """Настраивает стили для ttk виджетов."""
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Helvetica", 24, "bold"))
        style.configure("Status.TLabel", font=("Helvetica", 10))

    def create_widgets(self):
        """Создает все виджеты в окне."""
        # Главный контейнер с отступами
        main_frame = ttk.Frame(self.root, padding="30")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Заголовок
        title_label = ttk.Label(
            main_frame,
            text="🍅 Pomodoro Timer",
            style="Title.TLabel"
        )
        title_label.pack(pady=(0, 10))

        # Подзаголовок
        subtitle_label = ttk.Label(
            main_frame,
            text="Ваш помощник в управлении временем",
            font=("Helvetica", 10)
        )
        subtitle_label.pack(pady=(0, 30))

        # Компонент отображения таймера
        self.timer_display = TimerDisplay(main_frame)
        self.timer_display.pack(pady=20)

        # Фрейм для кнопок управления
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(pady=20)

        # Кнопки
        self.start_btn = ttk.Button(
            control_frame,
            text="▶ Старт",
            command=self._on_start,
            width=12
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.pause_btn = ttk.Button(
            control_frame,
            text="⏸ Пауза",
            command=self._on_pause,
            width=12,
            state=tk.DISABLED
        )
        self.pause_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = ttk.Button(
            control_frame,
            text="⟳ Сброс",
            command=self._on_reset,
            width=12
        )
        self.reset_btn.pack(side=tk.LEFT, padx=5)

        # Статусная строка
        self.status_label = ttk.Label(
            main_frame,
            text="✅ Готов к работе",
            style="Status.TLabel"
        )
        self.status_label.pack(pady=(20, 0))
        
        # Информация о циклах (добавим отдельно)
        self.cycle_label = ttk.Label(
            main_frame,
            text="Цикл: 0/4",
            font=("Helvetica", 10)
        )
        self.cycle_label.pack(pady=(5, 0))

    # === ОБНОВЛЕНИЕ ИНТЕРФЕЙСА ===

    def _update_initial_state(self):
        """Показывает начальное состояние."""
        # Показываем 25:00
        self.timer_display.update_time(25, 0)
        # Показываем статус
        self.status_label.config(text="✅ Готов к работе")
        self.cycle_label.config(text="Цикл: 0/4")

    def _update_time_display(self, time_str: str):
        """Обновляет отображение времени."""
        # time_str приходит в формате "MM:SS"
        minutes, seconds = map(int, time_str.split(':'))
        self.timer_display.update_time(minutes, seconds)

    def _update_status_display(self, status: str, cycle_count: int):
        """Обновляет отображение статуса и циклов."""
        # Обновляем статус
        status_icons = {
            "Работа завершена!": "🔴",
            "Короткий перерыв!": "🟢",
            "Длинный перерыв!": "🟣"
        }
        icon = status_icons.get(status, "✅")
        self.status_label.config(text=f"{icon} {status}")
        
        # Обновляем информацию о циклах
        self.cycle_label.config(text=f"Цикл: {cycle_count}/4")
        
        # Обновляем состояние кнопок
        self._update_buttons()

    def _update_buttons(self):
        """Обновляет состояние кнопок в зависимости от состояния таймера."""
        state = self.view_model.timer.timer_state
        
        if state.value == "idle":
            self.start_btn.config(state=tk.NORMAL)
            self.pause_btn.config(state=tk.DISABLED, text="⏸ Пауза")
        elif state.value == "running":
            self.start_btn.config(state=tk.DISABLED)
            self.pause_btn.config(state=tk.NORMAL, text="⏸ Пауза")
        elif state.value == "paused":
            self.start_btn.config(state=tk.DISABLED)
            self.pause_btn.config(state=tk.NORMAL, text="▶ Продолжить")
        elif state.value == "finished":
            self.start_btn.config(state=tk.NORMAL)
            self.pause_btn.config(state=tk.DISABLED, text="⏸ Пауза")

    # === ОБРАБОТЧИКИ КНОПОК ===

    def _on_start(self):
        """Обработчик нажатия кнопки Старт."""
        self.view_model.start()
        self._update_buttons()

    def _on_pause(self):
        """Обработчик нажатия кнопки Пауза."""
        state = self.view_model.timer.timer_state
        
        if state.value == "running":
            self.view_model.pause()
        elif state.value == "paused":
            self.view_model.resume()
        
        self._update_buttons()

    def _on_reset(self):
        """Обработчик нажатия кнопки Сброс."""
        self.view_model.reset()
        self._update_buttons()
        self._update_initial_state()