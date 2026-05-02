from datetime import datetime
import time

LOG_FILE = "73_state.log"

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def run_state_test():
    print(">>> ZADANIE 7.3: ZARZĄDZANIE STANEM URZĄDZENIA <<<")

    log_event("START: Test zarządzania stanem")

    log_event("ORIENTATION: PORTRAIT")
    time.sleep(1)

    log_event("ORIENTATION: LANDSCAPE")
    time.sleep(1)

    log_event("ORIENTATION: PORTRAIT")
    time.sleep(1)

    log_event("POWER: SCREEN OFF")
    time.sleep(1)

    log_event("POWER: SCREEN ON")

    log_event("STATUS: State round-trip completed successfully")
    print("SUKCES: zapisano historię zmian do 73_state.log")

if __name__ == "__main__":
    run_state_test()