from robot.api import logger
from selenium import webdriver

class Browser(object):

    instance = None
    driver = None
    
    def __new__(cls):

        if cls.instance is None:
            i = object.__new__(cls)
            cls.instance = i
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
        else:
            i = cls.instance
        return i