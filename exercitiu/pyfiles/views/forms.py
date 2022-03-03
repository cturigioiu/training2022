from main_page import MainPage
from elements_menu import SubElementsMenu

class FormsPage(MainPage):
    def __init__(self):
        super().__init__()
        super().select_category("Forms")
        self.subelements_menu = SubElementsMenu()
        
    def select_subcategory(self, category):
        self.subelements_menu.find_category(category).click()