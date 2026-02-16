import tkinter as tk

from model.timer import Timer
from viewmodel.timer_view_model import Time

class MenuWidget:
    """Класс, отвечающий за отрисовку и поведение меню"""
    def __init__(self, parent, app, timer, localization) -> None:
        self.parent = parent
        self.app = app
        self.localization = localization
        self.timer: Timer = timer

        self.menu_bar = tk.Menu(parent)
        self._setup_menu()
        parent.config(menu=self.menu_bar)

    def _setup_menu(self) -> None:
        """Отрисовка меню: установка кнопок, создание команд для них"""

        # === МЕНЮ "ПРЕСЕТЫ ВРЕМЕНИ" ===
        preset_menu = tk.Menu(self.menu_bar, tearoff=0)

        preset_menu.add_command(label='25/5/30', command=lambda: self.timer.change_preset(Time.TIME_25_05_30))
        preset_menu.add_command(label='15/3/20', command=lambda: self.timer.change_preset(Time.TIME_15_03_20))
        preset_menu.add_command(label='30/05/30', command=lambda: self.timer.change_preset(Time.TIME_30_05_30))
        preset_menu.add_command(label='30/10/25', command=lambda: self.timer.change_preset(Time.TIME_30_10_25))
        preset_menu.add_command(label='45/10/30', command=lambda: self.timer.change_preset(Time.TIME_45_10_30))
        preset_menu.add_command(label='50/15/30', command=lambda: self.timer.change_preset(Time.TIME_50_15_30))
        preset_menu.add_command(label='60/10/60', command=lambda: self.timer.change_preset(Time.TIME_60_10_60))
        preset_menu.add_command(label='180/30/60', command=lambda: self.timer.change_preset(Time.TIME_180_30_60))

        preset_menu.add_separator()
        
        preset_menu.add_command(label='DEBUG', command=lambda: self.timer.change_preset(Time.TIME_DEBUG))

        self.menu_bar.add_cascade(label=self.localization.get('menu_presets'), menu=preset_menu)

        # === МЕНЮ "ВИД" ===
        view_menu = tk.Menu(self.menu_bar, tearoff=0)
    
        theme_menu = tk.Menu(view_menu, tearoff=0)

        theme_menu.add_command(label=self.localization.get('menu_view_themes_light'), command=lambda: self.timer.change_theme('light'))
        theme_menu.add_command(label=self.localization.get('menu_view_themes_dark'), command=lambda: self.timer.change_theme('dark'))
        theme_menu.add_separator()
        theme_menu.add_command(label=self.localization.get('menu_view_themes_rose'), command=lambda: self.timer.change_theme('rose'))

        view_menu.add_cascade(label=self.localization.get('menu_view_themes'), menu=theme_menu)

        self.menu_bar.add_cascade(label=self.localization.get('menu_view'), menu=view_menu)

        # === МЕНЮ "Локализация" ===
        lang_menu = tk.Menu(self.menu_bar, tearoff=0)

        lang_menu.add_command(label="Русский", command=lambda: self.timer.change_language('ru'))
        lang_menu.add_command(label="English", command=lambda: self.timer.change_language('en'))

        self.menu_bar.add_cascade(label=self.localization.get('menu_language'), menu=lang_menu)
