from category_grid import CategoryGrid
from web_constants import WebConstants
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from browser import Browser
from robot.api import logger

class MainPage():
    def __init__(self):
        self.browser = Browser()
        self.browser.driver.get(WebConstants.BASE_PAGE_URL)
        self.category_grid = CategoryGrid()
        
    def select_category(self, category):
        element = self.browser.driver.find_element_by_xpath("//h5[contains(text(),'Book Store Application')]")
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(element).perform()
        self.category_grid.find_category(category).click()
        
