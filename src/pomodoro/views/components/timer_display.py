""" Компонент для отображения времени. """

import tkinter as tk
from tkinter import ttk

class TimerDisplay(ttk.Frame):
    """ Виджет для отображения времени в крупном формате. """

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.time_label = ttk.Label(
            master=self,
            text="25:00",
            font=("Helvetica", 64, "Bold")
        )
        self.time_label.pack()


        self.cycle_label = ttk.Label(
            master=self,
            text="Цикл: 0/4",
            font=("Helvetica", 12)
        )


    def update_timer(self, minutes: int, seconds: int):
        """ Обновляет отображаемое время. """
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.time_label.config(text=time_str)


    def update_cycle(self, current: int, total: int):
        """ Обновляет информацию о циклах. """
        self.cycle_label.config(text=f"Цикл: {current}/{total}")