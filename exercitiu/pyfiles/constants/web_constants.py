from robot.api import logger
from selenium import webdriver

class WebConstants:
    BASE_PAGE_URL = "https://demoqa.com/"
    CATEGORY_GRID_XPATH = "//h5"
    Elements_Menu_XPATH = "//div[@class='header-wrapper']//div[@class='header-text']"
    Sub_Elements_Menu_XPATH = "//div[@class='element-list collapse show']//span"
    Form_Fields_XPATH = "//form//div[contains(@id,'rapper')]"
    Form_Field_Title_XPATH = ".//div[@class='col-md-3 col-sm-12']"
    Form_Submit_XPATH = "//button[@type='submit']"
    Form_Verify_Title_XPATH = "//div[contains(text(),'Thanks for submitting the form')]"
    Form_Verify_Table_Row_XPATH = "//tbody/tr"
    Form_Verify_Table_Data_XPATH = ".//td"