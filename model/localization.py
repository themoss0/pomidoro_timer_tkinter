class Localization:
    """Класс, отвечающий за локализацию интерфейса"""
    TRANSLATIONS = {
        'ru': {
            # СТАТУСЫ
            'work': '💪 Работай!',
            'rest': '😴 Отдыхай!',
            'long_rest': '🎉 Длинный перерыв!',
            'pomidoro': '🍅 Помидоро',
            'paused': '⏸️ Пауза',
            # Окошко
            'app_title': 'Помидоро',
            # КНОПКИ
            'start_btn': 'Старт',
            'pause_btn': 'Пауза',
            'reset_btn': 'Ресет',

            # МЕНЮ
            'menu_presets': 'Пресеты',
            'menu_view': 'Вид',
            'menu_view_themes': 'Темы',
            'menu_view_themes_light': 'Светлая',
            'menu_view_themes_dark': 'Тёмная',
            'menu_view_themes_rose': 'Розовая',
            'menu_language': 'Язык'
        },
        'en': {
            # СТАТУСЫ
            'work': '💪 Work!',
            'rest': '😴 Rest!',
            'long_rest': '🎉 Long break!',
            'pomidoro': '🍅 Pomidoro',
            'paused': '⏸️ Pause',
            # Окошко
            'app_title': 'Pomidoro',
            # КНОПКИ
            'start_btn': 'Start',
            'pause_btn': 'Pause',
            'reset_btn': 'Reset',
            # МЕНЮ
            'menu_presets': 'Presets',
            'menu_view': 'View',
            'menu_view_themes': 'Themes',
            'menu_view_themes_light': 'Light',
            'menu_view_themes_dark': 'Dark',
            'menu_view_themes_rose': 'Rose',
            'menu_language': 'Language'
            
        }
    }

    def __init__(self, initial_lang='en'):
        self.lang_code = initial_lang

    def get(self, key: str):
        """Возвращает поле словаря по ключу, учитывая выбранный пользователем язык"""
        return self.TRANSLATIONS[self.lang_code].get(key, key)
    
    def set_language(self, new_lang_code: str):
        """Установка языка"""
        self.lang_code = new_lang_code