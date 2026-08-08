"""Главное окно приложения."""

import tkinter as tk
from tkinter import ttk
from pathlib import Path

from src.pomodoro.feature.timer.view.components.timer_display import TimerDisplay


class MainWindow:
    """Главное окно Pomodoro Timer."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("🍅 Pomodoro Timer")
        self.root.geometry("500x400")
        self.root.minsize(400, 300)

        # Пробуем установить иконку
        self._set_icon()

        self.center_window()
        self._setup_styles()
        self.create_widgets()

    def _set_icon(self):
        """Устанавливает иконку окна, если файл существует."""
        icon_path = Path(__file__).parent.parent.parent.parent / "assets" / "icons" / "tomato.png"
        if icon_path.exists():
            try:
                self.root.iconphoto(False, tk.PhotoImage(file=str(icon_path)))
            except Exception:
                pass  # Игнорируем ошибки с иконкой

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
            # command=self._on_start,
            width=12
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.pause_btn = ttk.Button(
            control_frame,
            text="⏸ Пауза",
            # command=self._on_pause,
            width=12,
            state=tk.DISABLED
        )
        self.pause_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = ttk.Button(
            control_frame,
            text="⟳ Сброс",
            # command=self._on_reset,
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