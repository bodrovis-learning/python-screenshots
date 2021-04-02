import keyboard
import pyautogui
from datetime import datetime
import os
import sys


class Screenshot:
    STOP_COMBINATION = "ctrl+shift+x"

    def __init__(self, dir: str) -> None:
        self.path = os.path.join(os.getcwd(), dir)

    def run(self) -> None:
        self.__create_path_if_absent()
        keyboard.on_press(self.__keyboard_callback)
        keyboard.wait(self.STOP_COMBINATION)

    def __create_path_if_absent(self):
        if not os.path.exists(self.path):
            try:
                os.makedirs(self.path)
            except Exception as e:
                print(e)
                # Check https://github.com/boppreh/keyboard/issues/167
                os._exit(0)

    def __keyboard_callback(
            self, event: keyboard._keyboard_event.KeyboardEvent) -> None:
        if event.name == "`":
            self.__create_screenshot()

    def __create_screenshot(self) -> None:
        self.__create_path_if_absent()

        name = datetime.now().strftime("%d-%m-%Y_%H_%M_%S_%f")
        pyautogui.screenshot().save(os.path.join(self.path, f"{name}.png"))


if __name__ == "__main__":
    dir = 'screens' if len(sys.argv) < 2 else sys.argv[1]
    screen = Screenshot(dir)
    screen.run()
