import os.path
import time
import win32con
import win32gui
import win32process
from pykeyboard import PyKeyboard

# ERROR_CODE
FILE_NOT_EXIST = 404


class GameWindow:
    def __init__(self, game, keyboard: PyKeyboard):
        self._game = game
        self._keyboard = keyboard

        process_id = win32process.GetWindowThreadProcessId(self._game)
        print(process_id)

        if win32gui.IsIconic(self._game):
            print(1)
            win32gui.ShowWindow(self._game, win32con.SW_SHOWMINIMIZED)
            win32gui.ShowWindow(self._game, win32con.SW_NORMAL)
        else:
            print(2)
            win32gui.ShowWindow(self._game, win32con.SW_SHOWMINIMIZED)
            win32gui.ShowWindow(self._game, win32con.SW_NORMAL)

    def press_key(self, k: str):
        while win32gui.IsIconic(self._game):
            time.sleep(3)
        self._keyboard.press_key(k)
        self._keyboard.release_key(k)
        pass


def map_alpha(phonetic):
    print(phonetic)
    if phonetic == "+1":
        return "q"
    elif phonetic == "+2":
        return "w"
    elif phonetic == "+3":
        return "e"
    elif phonetic == "+4":
        return "r"
    elif phonetic == "+5":
        return "t"
    elif phonetic == "+6":
        return "y"
    elif phonetic == "+7":
        return "u"
    elif phonetic == "1":
        return "a"
    elif phonetic == "2":
        return "s"
    elif phonetic == "3":
        return "d"
    elif phonetic == "4":
        return "f"
    elif phonetic == "5":
        return "g"
    elif phonetic == "6":
        return "h"
    elif phonetic == "7":
        return "j"
    elif phonetic == "-1":
        return "z"
    elif phonetic == "-2":
        return "x"
    elif phonetic == "-3":
        return "c"
    elif phonetic == "-4":
        return "v"
    elif phonetic == "-5":
        return "b"
    elif phonetic == "-6":
        return "n"
    elif phonetic == "-7":
        return "m"
    else:
        raise Exception("Not in mapper.")


def byte_dance_1(op: GameWindow, music_file: str):
    if os.path.exists(music_file):
        with open(music_file, "r") as f:
            chart = f.read()

        for byte in list(chart):
            if byte == " ":
                time.sleep(0.085)
            elif byte == "\n":
                time.sleep(0.34)
            else:
                op.press_key(byte)
    else:
        return FILE_NOT_EXIST


def byte_dance_2(op: GameWindow, music_file: str):
    alpha = ""
    if os.path.exists(music_file):
        with open(music_file, "r") as f:
            chart = f.read()

        for byte in list(chart):
            if byte == " ":
                time.sleep(0.092)
            elif byte == "-" or byte == "+":
                alpha += byte
            elif byte == "\n":
                time.sleep(0.34)
            elif byte == "(" or byte == ")":
                continue
            else:
                alpha += byte
                op.press_key(map_alpha(alpha))
                alpha = ""
    else:
        return FILE_NOT_EXIST


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    handle = win32gui.FindWindow(None, u"原神")
    my_keyboard = PyKeyboard()
    game_window = GameWindow(handle, my_keyboard)
    # byte_dance_1(game_window, music_file=u"生生世世爱")
    byte_dance_2(game_window, music_file=u"起风了")
