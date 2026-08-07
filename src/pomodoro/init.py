import sys
import tkinter as tk
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pomodoro.views.main_window import MainWindow


def main():
    """ Запускает главное окно приложения """
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()