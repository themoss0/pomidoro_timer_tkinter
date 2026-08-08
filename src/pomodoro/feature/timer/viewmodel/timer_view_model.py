"""Посредник между моделью и отображением таймера."""
from enum import Enum
from src.pomodoro.feature.timer.model.timer import Timer, IntervalType


class Preset(Enum):
    """Доступные пресеты времени."""
    CLASSIC = (25, 5, 30, 4)      # 25/5/30, 4 цикла
    SHORT = (30, 5, 30, 4)        # 30/5/30, 4 цикла
    LONG = (60, 10, 60, 4)        # 60/10/60, 4 цикла
    EXTREME = (180, 30, 60, 4)    # 180/30/60, 4 цикла
    DEBUG = (1, 1, 2, 2)          # Для тестирования


class TimerViewModel:
    """Класс ViewModel таймера."""
    
    def __init__(self, root):
        self.root = root

        # Создаём модель
        self.timer = Timer()

        # Устанавливаем колбэки
        self.timer.set_on_tick(self._on_tick)
        self.timer.set_on_interval_end(self._on_interval_end)

        # ID события after
        self._after_id = None
        
        # Колбэки для View (будут установлены извне)
        self.on_display_update = None
        self.on_status_update = None

    # === Бизнес-логика ===

    def _on_tick(self, remaining_seconds):
        """Обновляет отображение."""
        # Преобразуем секунды в минуты:секунды
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        time_str = f"{minutes:02d}:{seconds:02d}"  # Исправлено!

        # Обновляем интерфейс
        if self.on_display_update:
            self.on_display_update(time_str)

    def _on_interval_end(self, interval_type, cycle_count):
        """Вызывается моделью при завершении интервала."""
        # Определяем текст для статуса
        if interval_type == IntervalType.INTERVAL_WORK:
            status = "Работа завершена!"
        elif interval_type == IntervalType.INTERVAL_SHORT_BREAK:
            status = "Короткий перерыв!"
        else:
            status = "Длинный перерыв!"
        
        # Обновляем интерфейс
        if self.on_status_update:
            self.on_status_update(status, cycle_count)
        
        # Останавливаем цикл обновления
        self._stop_timer_loop()


    def set_callbacks(self, on_display_update=None, on_status_update=None):
        """Устанавливает колбэки для обновления интерфейса."""
        self.on_display_update = on_display_update
        self.on_status_update = on_status_update

    # === Взаимодействие ===

    def start(self):
        """Запускает таймер."""
        self.timer.start()
        self._start_timer_loop()

    def pause(self):
        """Приостанавливает таймер."""
        self.timer.pause()
        self._stop_timer_loop()

    def resume(self):
        """Продолжает работу таймера."""
        self.timer.resume()
        self._start_timer_loop()

    def reset(self):
        """Сбрасывает время таймера."""
        self.timer.reset()  # Исправлено!
        self._stop_timer_loop()

    # === ОБНОВЛЕНИЕ ЭКРАНА ===

    def _tick_loop(self):
        """Рекурсивный цикл обновления каждую секунду."""
        # Вызываем tick у модели
        self.timer.tick()

        # Планируем следующий вызов через 1000 мс
        self._after_id = self.root.after(1000, self._tick_loop)

    def _start_timer_loop(self):
        """Запускает цикл обновления."""
        self._stop_timer_loop()
        self._tick_loop()

    def _stop_timer_loop(self):
        """Останавливает цикл обновления."""
        if self._after_id:
            self.root.after_cancel(self._after_id)
            self._after_id = None