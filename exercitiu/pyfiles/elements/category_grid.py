from web_constants import WebConstants
from browser import Browser
from selenium.webdriver.common.by import By

class CategoryGrid():
    def __init__(self):

        self.elements = None
        self.get_elements()
    
    def get_elements(self):
        self.elements = Browser.driver.find_elements(By.XPATH, WebConstants.CATEGORY_GRID_XPATH)
        
    def find_category(self, category):
        for elm in self.elements:
            if category == elm.get_property('innerHTML'):
                return elm
        return None
        
        
        