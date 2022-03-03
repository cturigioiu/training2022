from forms import FormsPage
from browser import Browser
from web_constants import WebConstants
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from robot.api import logger
from robot.api.deco import keyword
import re

class PracticeForm(FormsPage):
    def __init__(self):
        super().__init__()
        super().select_subcategory("Practice Form")
        self.fields = self.get_input_fields()
        
    def get_input_fields(self):
        logger.console("Trying to get input fields.")
        return self.browser.driver.find_elements_by_xpath(WebConstants.Form_Fields_XPATH)
        logger.console("Input fields retrieved.")

    def get_input_type(self, input):
        return input.get_property('type')
    
    @keyword('Form Fill ${d}')
    def fill_input_field(self, d):
        logger.console("Trying to fill input fields.")
        self.browser.driver.find_element(By.XPATH, "//div[contains(text(),'Elements')]").click()
        
        for field in self.fields:
            title = field.find_element(By.XPATH,WebConstants.Form_Field_Title_XPATH)
    
            labels = field.find_elements(By.XPATH,".//label")
            inputs = field.find_elements(By.XPATH,".//input") + field.find_elements(By.XPATH,".//textarea")
            
            actions = ActionChains(self.browser.driver)
            actions.move_to_element(title).perform()
            
            title_name = title.get_property('innerText')
            if '(' in title_name:
                title_name = title_name[:title_name.index('(')]
    
            if title_name not in d.keys():
                continue
            else:
                needs_split = False
                if len(labels) < len(inputs):
                    needs_split = True
                if all([self.get_input_type(input)=='text' for input in inputs]):
                    self.fill_text_field(data=d[title_name], inputs=inputs, needs_split=needs_split)
                    continue
                if all([input.get_property('localName')=='textarea' for input in inputs]):
                    self.fill_text_field(data=d[title_name], inputs=inputs, needs_split=needs_split)
                    continue
                if all([self.get_input_type(input)=='radio' for input in inputs]):
                    self.select_field(data=d[title_name], labels=labels)
                    continue
                if all([self.get_input_type(input)=='checkbox' for input in inputs]):
                    self.select_field(data=d[title_name], labels=labels)
                    continue
        logger.console("Input fields filled.")
                    
    def fill_text_field(self, data, inputs, needs_split):
        
        if needs_split:
            data = data.split(" ")
            if inputs[0].get_attribute('ariaAutoComplete') == 'list':
                for i in range(len(inputs)):
                    inputs[i].send_keys(data[i])
                    inputs[i].send_keys(Keys.RETURN)
            else:
                for i in range(len(inputs)):
                    inputs[i].send_keys(Keys.CONTROL,'a')
                    inputs[i].send_keys(data[i])
        else:
            if inputs[0].get_attribute('ariaAutoComplete') == 'list':
                inputs[0].send_keys(Keys.CONTROL,'a')
                for entry in data:
                    inputs[0].send_keys(entry)
                    inputs[0].send_keys(Keys.RETURN)
            else:
                inputs[0].send_keys(Keys.CONTROL,'a')
                inputs[0].send_keys(data)
            
    def select_field(self, data, labels):
        for label in labels:
            if label.get_property('innerHTML') in data:
                label.click()
    
    @keyword('Form Submit')    
    def submit_form(self):
        button = self.browser.driver.find_element(By.XPATH, WebConstants.Form_Submit_XPATH)
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(button).perform()
        button.send_keys(Keys.RETURN)
    
    def retrieve_data_from_table(self):
        returned_dict = {}
        rows = self.browser.driver.find_elements(By.XPATH, WebConstants.Form_Verify_Table_Row_XPATH)
        for row in rows:
            key, value = row.find_elements(By.XPATH, WebConstants.Form_Verify_Table_Data_XPATH)
            returned_dict[key.get_property('innerText')] = value.get_property('innerText')
        return returned_dict
    
    def compare_data(self, expected_data, observed_data):
        logger.console("Compare data in table.")
        validation_list = []
        for expected_key in expected_data.keys():
            validation = False
            for observed_key in observed_data.keys():
                if expected_key in observed_key or observed_key in expected_key:
                    validation = True
                    break
            validation_list.append(validation)
        return all(validation_list)
    
    @keyword('Form Verify ${expected_data}')
    def verify(self, expected_data):
        logger.console("Check if form was submitted.")
        if not self.browser.driver.find_element(By.XPATH, WebConstants.Form_Verify_Title_XPATH):
            return Flase
        logger.console("Get observed data.")
        observed_data = self.retrieve_data_from_table()

        return self.compare_data(expected_data, observed_data)
    
