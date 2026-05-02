import json

class BasePage:
    def __init__(self, selectors_file="../Artefakt05/53_selectors.json"):
        with open(selectors_file, "r", encoding="utf-8") as f:
            self.selectors = json.load(f)

        print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(self.selectors)} elementów.")

    def get_selector(self, business_name):
        return self.selectors.get(business_name)

# test uruchomieniowy
if __name__ == "__main__":
    page = BasePage()
    test = page.get_selector("ADD")  # możesz zmienić na coś z JSON
    print(f"Weryfikacja klucza 'ADD': {test}")