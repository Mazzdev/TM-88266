from MainPage import MainPage

def run_pom_test():
    print(">>> ZADANIE 6.3: TEST SCENARIUSZA W ARCHITEKTURZE POM <<<")

    page = MainPage()

    print("\n--- PRZEBIEG SCENARIUSZA TESTOWEGO ---")

    print("KROK 1: Sprawdzenie widoczności tytułu")
    page.check_title_visibility()

    print("KROK 2: Kliknięcie w przycisk ADD")
    page.click_add_button()

    print("KROK 3: Kliknięcie w element IMAGE")
    page.click_image()

    print("\n[OK] Scenariusz wykonany sukcesem.")

if __name__ == "__main__":
    run_pom_test()