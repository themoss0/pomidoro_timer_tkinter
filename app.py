
import tkinter as tk
import os
from os import sys

from model.localization import Localization
from model.theme_manager import ThemeManager
from model.timer import Timer
from viewmodel.timer_view_model import State, Time, TimerViewModel
from widgets.menu_widget import MenuWidget

class Config:
    """Класс, задающий основные конфигурации окну приложения"""
    WINDOW_SIZE='300x400'
    WINDOW_TITLE='Pomidoro'

class Application:
    """Класс приложения. Здесь идёт создание приложения, настройка всех дочерних классу Timer классов(Localization, ThemeManager)"""
    def __init__(self):
        self.app=tk.Tk()
        self.app.resizable(False, False)

        self._set_icon()
        self._setup_window()

        self.localization: Localization = Localization('ru')

        self.theme_manager: ThemeManager = ThemeManager(self.app, current_theme='light')
        self.theme_manager.apply_theme(self.app, self.theme_manager.current_theme, '__init__')

        timevm = TimerViewModel(default_state=State.IDLE, time_interval=Time.TIME_25_05_30)
        self.timer: Timer = Timer(parent=self.app, timervm=timevm, theme_manager=self.theme_manager, localization=self.localization)

        self.timer.set_theme_manager(self.theme_manager)
        self.timer.set_localization(self.localization)
        
        self._setup_menu()
        self.app.menu = self.menu

        self._setup_timer()


    def _resource_path(self, relative_path):
        """Универсальный путь для .py и .exe"""
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_path, relative_path)
    
    def _set_icon(self):
        """Ставим иконку (работает и в .py, и в .exe)"""
        try:
            # Конвертируем .ico в .png заранее (один раз)
            # И кладём рядом с main.py
            icon_path = self._resource_path('pomidor.png')
            
            if os.path.exists(icon_path):
                icon = tk.PhotoImage(file=icon_path)
                self.app.iconphoto(True, icon)
                print(f"✅ Иконка загружена: {icon_path}")
            else:
                print(f"⚠️ Иконка не найдена: {icon_path}")
        except Exception as e:
            print(f"⚠️ Иконка не загружена: {e}")


    def _setup_window(self):
        """Настройка окна. Размеры, заголовок"""
        self.app.title(Config.WINDOW_TITLE)
        self.app.geometry(Config.WINDOW_SIZE)

    def _setup_timer(self):
        """Расположение на экране объекта класса Timer"""
        self.timer.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    def _setup_menu(self):
        """ Создание меню """
        self.menu = MenuWidget(parent=self.app, app=self, timer=self.timer, localization=self.localization)
        self.app.menu = self.menu

    def run(self):
        """Запуск приложения"""
        self.app.mainloop()