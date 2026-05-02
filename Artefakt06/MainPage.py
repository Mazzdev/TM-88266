from BasePage import BasePage

class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        print("[MAIN_PAGE] Ekran główny zainicjalizowany.")

    def find_id(self, business_name):
        selector = self.get_selector(business_name)

        if selector:
            return selector["value"]

        return None

    def click_add_button(self):
        element_id = self.find_id("ADD")

        if element_id:
            print(f"SUKCES: Wykonano kliknięcie w element UI o ID: '{element_id}'")
        else:
            print("ERROR: Selector ADD not found")

    def check_title_visibility(self):
        element_id = self.find_id("ACTION_BAR_TITLE")

        if element_id:
            print(f"SUKCES: Odnaleziono nagłówek strony o ID: '{element_id}'")
        else:
            print("ERROR: Selector ACTION_BAR_TITLE not found")

    def click_image(self):
        element_id = self.find_id("IMAGE")

        if element_id:
            print(f"SUKCES: Wykonano kliknięcie w element UI o ID: '{element_id}'")
        else:
            print("ERROR: Selector IMAGE not found")


if __name__ == "__main__":
    page = MainPage()
    page.click_add_button()
    page.check_title_visibility()
    page.click_image()