""" Модель таймера. """

from enum import Enum


class TimerState(Enum):
    """ Состояния таймера. """
    IDLE="idle"
    RUNNING="running"
    PAUSED="paused"
    FINISHED='finished'


class IntervalType(Enum):
    """ Интервалы таймера """
    INTERVAL_WORK="work"
    INTERVAL_SHORT_BREAK="short_break"
    INTERVAL_LONG_BREAK="long_break"

class Timer:
    """ Класс таймера. """

    def __init__(self, work_duration=25, short_break=5, long_break=30, cycles_before_long=4):
        """
        Инициализация модели таймера.
    
         Args:
            work_duration: Длительность работы в минутах (по умолчанию 25)
            short_break: Длительность короткого перерыва в минутах (по умолчанию 5)
            long_break: Длительность длинного перерыва в минутах (по умолчанию 30)
            cycles_before_long: Количество циклов до длинного перерыва (по умолчанию 4)
        """
        # Настройки
        self.work_duration = work_duration
        self.short_break = short_break
        self.long_break = long_break
        self.cycles_before_long = cycles_before_long

        # Состояние
        self.timer_state = TimerState.IDLE
        self.current_interval = IntervalType.INTERVAL_WORK
        self.cycle_count = 0
        self.elapsed_seconds = 0

    # === ВЗАИМОДЕЙСТВИЕ ===

    def set_on_tick(self, callback):
        """Устанавливает колбэк на каждый тик таймера."""
        self._on_tick = callback
    
    def set_on_interval_end(self, callback):
        """Устанавливает колбэк на завершение интервала."""
        self._on_interval_end = callback


    @property
    def remaining_seconds(self):
        """Оставшееся время в секундах."""
        return self.total_seconds - self.elapsed_seconds


    @property
    def total_seconds(self):
        """ Общая длительность интервала в секундах. """
        if self.current_interval == IntervalType.INTERVAL_WORK:
            return self.work_duration * 60
        elif self.current_interval == IntervalType.INTERVAL_SHORT_BREAK:
            return self.short_break * 60
        else:
            return self.long_break * 60

    # === ПОВЕДЕНИЕ ===        

    def start(self):
        """ Запускает таймер. """
        if self.timer_state == TimerState.IDLE:
            self.timer_state = TimerState.RUNNING


    def pause(self):
        """ Приостанавливает таймер. """
        if self.timer_state == TimerState.RUNNING:
            self.timer_state = TimerState.PAUSED


    def resume(self):
        """ Продолжает работу таймера. """
        if self.timer_state == TimerState.PAUSED:
            self.timer_state = TimerState.RUNNING


    def reset(self):
        """ Сбрасывает время таймера."""
        self.timer_state = TimerState.IDLE
        self.current_interval = IntervalType.INTERVAL_WORK
        self.cycle_count = 0
        self.elapsed_seconds = 0

        if self._on_tick:
            self._on_tick(self.remaining_seconds)


    def tick(self):
        """
        Обновляет состояние таймера на 1 секунду.
        """
        if self.timer_state != TimerState.RUNNING:
            return

        self.elapsed_seconds += 1

        # Вызываем колбэк, если он есть
        if self._on_tick:
            self._on_tick(self.remaining_seconds)
        
        # Проверяем, не закончился ли интервал
        if self.elapsed_seconds >= self.total_seconds:
            self._on_interval_end()


    def _switch_interval(self):
        """ Переключает на следующий интервал. """
        if self.current_interval == IntervalType.INTERVAL_WORK:
            # Работа завершена -> переключаемся на перерыв
            self.cycle_count += 1

            if self.cycle_count >= self.cycles_before_long:
                self.current_interval = IntervalType.INTERVAL_LONG_BREAK
            else:
                self.current_interval = IntervalType.INTERVAL_SHORT_BREAK

        elif self.current_interval == IntervalType.INTERVAL_SHORT_BREAK:
            # Короткий перерыв завершен -> снова работа
            self.current_interval = IntervalType.INTERVAL_WORK

        elif self.current_interval == IntervalType.INTERVAL_LONG_BREAK:
            # Длинный перерыв завершён -> работа, цикл начинается заново
            self.cycle_count = 0
            self.current_interval = IntervalType.INTERVAL_WORK

        # Сбрасываем время для нового интервала
        self.elapsed_seconds = 0


    def _on_interval_end(self):
        """Вызывается, когда текущий интервал завершен."""
        # Переключаем интервал
        self._switch_interval()
    
        # Останавливаем таймер
        self.timer_state = TimerState.IDLE
    
        # Вызываем колбэки
        if self._on_interval_end:
            self._on_interval_end(self.current_interval, self.cycle_count)
    
        # ОБЯЗАТЕЛЬНО обновляем отображение!
        if self._on_tick:
            self._on_tick(self.remaining_seconds)



