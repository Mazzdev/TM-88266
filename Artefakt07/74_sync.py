import sys
import os
import time

sys.path.append(os.path.abspath("../Artefakt06"))

from MainPage import MainPage


class WebDriverWait:
    def __init__(self, timeout):
        self.timeout = timeout

    def until(self, condition):
        start = time.time()

        while time.time() - start < self.timeout:
            if condition():
                return True
            time.sleep(0.5)

        raise TimeoutError("Element nie został znaleziony w czasie timeout")


class SyncManager(MainPage):
    def __init__(self):
        super().__init__()

    def wait_for_element(self, business_name, timeout=5):
        print(">>> ZADANIE 7.4: SYNCHRONIZACJA / EXPLICIT WAIT <<<")
        print(f"[SYNC] Rozpoczynam oczekiwanie na: {business_name}, timeout={timeout}s")

        start = time.time()

        try:
            wait = WebDriverWait(timeout)
            wait.until(lambda: self.find_id(business_name) is not None)

            elapsed = round(time.time() - start, 2)
            element_id = self.find_id(business_name)

            print(f"SUKCES: Element '{business_name}' znaleziony po {elapsed}s")
            print(f"SUKCES: ID elementu: {element_id}")

        except TimeoutError:
            elapsed = round(time.time() - start, 2)
            print(f"TIMEOUT: Nie znaleziono elementu '{business_name}' po {elapsed}s")


if __name__ == "__main__":
    sync = SyncManager()
    sync.wait_for_element("ADD", timeout=5)
    sync.wait_for_element("NON_EXISTENT_BUTTON", timeout=3)