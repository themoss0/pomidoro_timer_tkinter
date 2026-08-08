"""Компонент для отображения времени."""

import tkinter as tk
from tkinter import ttk


class TimerDisplay(ttk.Frame):
    """Виджет для отображения времени в крупном формате."""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.time_label = ttk.Label(
            self,
            text="25:00",
            font=("Helvetica", 64, "bold")
        )
        self.time_label.pack()

    def update_time(self, minutes: int, seconds: int):
        """Обновляет отображаемое время."""
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.time_label.config(text=time_str)