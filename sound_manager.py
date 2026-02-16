import gc
import os
import sys
from playsound3 import playsound

class SoundManager:
    """Менеджер звуков - работает и в .py, и в .exe"""
    
    def __init__(self):
        self.sounds = {}
        self._load_sounds()
    
    def _resource_path(self, relative_path) -> str:
        """Получить путь к файлу в .exe или .py"""
        try:
            # Для .exe: pyinstaller создает временную папку _MEIPASS
            base_path = sys._MEIPASS
        except AttributeError:
            # Для .py: берем путь к текущему файлу
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        return os.path.join(base_path, relative_path)
    
    def _load_sounds(self):
        """Загрузить все звуки (с обработкой ошибок)"""
        sound_files = {
            'interval': 'core\\data\\audio\\interval_audio.mp3',
            'warning': 'core\\data\\audio\\warning_audio.mp3',
        }
        
        for name, path in sound_files.items():
            try:
                full_path = self._resource_path(path)
                # Проверяем, существует ли файл
                if os.path.exists(full_path):
                    self.sounds[name] = full_path
                    print(f"✅ Звук загружен: {name} -> {full_path}")
                else:
                    print(f"⚠️ Файл не найден: {full_path}")
            except Exception as e:
                print(f"❌ Ошибка загрузки {name}: {e}")
    
    def play(self, sound_name, block=False) -> bool:
        """Воспроизвести звук"""
        if sound_name in self.sounds:
            try:
                playsound(self.sounds[sound_name], block=block)
                return True
            except Exception as e:
                print(f"❌ Ошибка воспроизведения {sound_name}: {e}")
        else:
            print(f"⚠️ Звук не найден: {sound_name}")
        return False
    
    def play_async(self, sound_name) -> bool:
        """Асинхронное воспроизведение (по умолчанию)"""
        return self.play(sound_name, block=False)
    
    def __del__(self):
        self.sounds.clear()
        gc.collect()

# Глобальный экземпляр (синглтон)
_sound_manager = None

def get_sound_manager():
    """Получить экземпляр SoundManager (создать при первом вызове)"""
    global _sound_manager
    if _sound_manager is None:
        _sound_manager = SoundManager()
    return _sound_manager