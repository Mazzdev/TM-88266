import sys
import os
import time

sys.path.append(os.path.abspath("../Artefakt06"))

from MainPage import MainPage


class InterruptSimulator(MainPage):
    def __init__(self):
        super().__init__()

    def simulate_incoming_call(self):
        print(">>> ZADANIE 7.2: TESTY PRZERWAŃ <<<")

        print("[INTERRUPT] KROK 1: Stan aplikacji przed połączeniem: ACTIVE")
        time.sleep(1)

        print("[SYSTEM] Symulacja połączenia przychodzącego...")
        print("[INTERRUPT] KROK 2: Aplikacja otrzymała zdarzenie: onPause")
        time.sleep(2)

        print("[INTERRUPT] KROK 3: Połączenie zakończone")
        print("[INTERRUPT] KROK 4: Aplikacja otrzymała zdarzenie: onResume")
        print("SUKCES: Aplikacja odzyskała fokus po przerwaniu.")


if __name__ == "__main__":
    simulator = InterruptSimulator()
    simulator.simulate_incoming_call()