from web_constants import WebConstants
from browser import Browser
from selenium.webdriver.common.by import By
from robot.api import logger

class ElementsMenu():
    def __init__(self):
        self.elements = None
        self.get_elements()
    
    def get_elements(self):
        self.elements = Browser.driver.find_elements(By.XPATH, WebConstants.Elements_Menu_XPATH)
        
    def find_category(self, category):
        for elm in self.elements:
            if category == elm.get_property('innerHTML'):
                return elm
        return None
        
class SubElementsMenu():
    def __init__(self):
        self.elements = None
        self.get_elements()
    
    def get_elements(self):
        self.elements = Browser.driver.find_elements(By.XPATH, WebConstants.Sub_Elements_Menu_XPATH)
        
    def find_category(self, category):
        for elm in self.elements:
            logger.console(elm.get_property('innerHTML'))
        
            if category == elm.get_property('innerHTML'):
                return elm
        return None
        
        