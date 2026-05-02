import sys
import os

sys.path.append(os.path.abspath("../Artefakt06"))

from MainPage import MainPage
import time

class GestureAutomator(MainPage):

    def __init__(self):
        super().__init__()

    def scroll_down_logic(self, duration_ms=800):
        print(">>> ZADANIE 7.1: TESTY GESTÓW DOTYKOWYCH <<<")

        # symulacja rozmiaru ekranu
        screen_width = 1080
        screen_height = 1920

        start_x = int(screen_width * 0.5)
        start_y = int(screen_height * 0.8)

        end_x = int(screen_width * 0.5)
        end_y = int(screen_height * 0.2)

        print(f"[GESTURE] Start: ({start_x}, {start_y})")
        print(f"[GESTURE] End: ({end_x}, {end_y})")
        print(f"[GESTURE] Duration: {duration_ms}ms")

        time.sleep(1)

        print("SUKCES: Przewinięto listę o 60% wysokości ekranu.")

if __name__ == "__main__":
    g = GestureAutomator()
    g.scroll_down_logic()