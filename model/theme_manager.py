import tkinter as tk

class ThemeManager:
    """Класс, отвечающий за отрисовку цветов(тем) приложения"""
    THEMES = {
        'light': {
            'bg': '#ffffff',
            'fg': '#000000',

            'button_bg': '#f0f0f0',
            'button_fg': '#000000',

            'start_bg': '#4CAF50',      # Зелёный
            'start_fg': '#ffffff',       # Белый текст
            'pause_bg': '#FF9800',       # Оранжевый
            'pause_fg': '#ffffff',       # Белый текст
            'reset_bg': '#f44336',       # Красный
            'reset_fg': '#ffffff',


            'status_work': '#ff0000',
            'status_rest': '#00aa00',
            'status_long_rest': '#aa00aa',
            'status_paused': '#666666',      
            'status_idle': '#000000',
        },
        'dark': {
            'bg': '#2b2b2b',
            'fg': '#ffffff',

            'button_bg': '#3c3c3c',
            'button_fg': '#ffffff',

            'start_bg': '#2E7D32',       # Тёмно-зелёный
            'start_fg': '#ffffff',
            'pause_bg': '#B26A00',       # Тёмно-оранжевый
            'pause_fg': '#ffffff',
            'reset_bg': '#B71C1C',       # Тёмно-красный
            'reset_fg': '#ffffff',

            'status_work': '#ff6666',
            'status_rest': '#66ff66',
            'status_long_rest': '#cc66ff',
            'status_paused': '#aaaaaa',
            'status_idle': '#ffffff',
        },

        'rose': {
            # Базовые цвета - нежный розовый фон
            'bg': '#fff0f5',      # Розово-белый (лавэндер блаш)
            'fg': '#8b4c6f',       # Тёмно-розовый для текста
            
            # Общие цвета кнопок (запасной вариант)
            'button_bg': '#ffb6c1',  # Светло-розовый
            'button_fg': '#8b4c6f',   # Тёмно-розовый текст
            
            # ИНДИВИДУАЛЬНЫЕ ЦВЕТА КНОПОК В РОЗОВОЙ ТЕМЕ
            'start_bg': '#ff8a9f',    # Нежно-розовый
            'start_fg': '#ffffff',     # Белый текст
            'pause_bg': '#d291bc',     # Сиреневый
            'pause_fg': '#ffffff',     # Белый текст
            'reset_bg': '#c06c84',     # Тёмно-розовый
            'reset_fg': '#ffffff',     # Белый текст
            
            # СТАТУСЫ В РОЗОВОЙ ТЕМЕ
            'status_work': '#c44569',   # Розово-красный (работа)
            'status_rest': '#9b6b9b',   # Сиреневый (отдых)
            'status_long_rest': '#e667af',  # Фуксия (длинный отдых)
            'status_paused': '#ac8c8c',     # Серо-розовый (пауза)
            'status_idle': '#8b4c6f',       # Тёмно-розовый (ожидание)
            
            # ДОПОЛНИТЕЛЬНЫЕ РОЗОВЫЕ ОТТЕНКИ
            'heart': '#ff6b8b',        # Цвет сердечка
            'highlight': '#ffe4ec',    # Подсветка
            'border': '#d9b4c4',       # Розовая рамка
        }
    }

    def __init__(self, root, current_theme='light'):
        self.root = root
        self.current_theme = current_theme

    def apply_theme(self, widget, theme_name: str, source='unknown'):
        """Применение темы по названию"""
        print(f"\n🎨 apply_theme({theme_name}) вызван из: {source}")
        self.current_theme = theme_name
        theme = self.THEMES[theme_name]
        self._apply_theme_to_widget(widget, theme)

    def get(self, key: str):
        """Получение поля словаря по ключу, учитывая выбранную пользователем тему"""
        return self.THEMES[self.current_theme].get(key, key)

    def _apply_theme_to_widget(self, widget, theme):
        """Рекурсивная функция, которая перебирает каждый виджет экрана и перерисовывает их согласно цвету темы"""
        try:
            widget_type = widget.__class__.__name__
            print(f"  📦 Обрабатываю {widget_type}")
        
            if isinstance(widget, tk.Tk):
                widget.configure(bg=theme['bg'])
                print(f"    ✓ Tk: bg={theme['bg']}")
            elif isinstance(widget, tk.Label):
                widget.config(bg=theme['bg'], fg=theme['fg'])
                print(f"    ✓ Label: bg={theme['bg']}, fg={theme['fg']}")
            elif isinstance(widget, tk.Button):
                widget.config(bg=theme['button_bg'], fg=theme['button_fg'])
                print(f"    ✓ Button: bg={theme['button_bg']}, fg={theme['button_fg']}")
            elif isinstance(widget, tk.Frame):
                widget.config(bg=theme['bg'])
                print(f"    ✓ Frame: bg={theme['bg']}")
            elif isinstance(widget, tk.Listbox):
                widget.config(bg=theme['bg'], fg=theme['fg'])
                print(f"    ✓ Listbox: bg={theme['bg']}, fg={theme['fg']}")
            elif isinstance(widget, tk.Menu):
                widget.config(bg=theme['bg'], fg=theme['fg'])
                print(f"    ✓ Menu: bg={theme['bg']}, fg={theme['fg']}")
            elif isinstance(widget, tk.PanedWindow):
                widget.config(bg=theme['bg'])
                print(f"    ✓ PanedWindow: bg={theme['bg']}")
            else:
                print(f"    ? Неизвестный тип: {widget_type}")
        except Exception as e:
            print(f"    ❌ Ошибка: {e}")

        for child in widget.winfo_children():
            self._apply_theme_to_widget(child, theme)