from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DynamicValuesScreen(object):

    SEND_TEXT_KEY = 'com.example.androidsampleapp.qa:id/textKey'
    SEND_TEXT_VALUE = 'com.example.androidsampleapp.qa:id/textValue'
    SEND_TEXT_BUTTON = 'com.example.androidsampleapp.qa:id/sendText'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.send_text_key = self.wait.until(EC.visibility_of_element_located((By.ID, self.SEND_TEXT_KEY)))
        self.send_text_value = self.wait.until(EC.visibility_of_element_located((By.ID, self.SEND_TEXT_VALUE)))
        self.send_text_button = self.wait.until(EC.visibility_of_element_located((By.ID, self.SEND_TEXT_BUTTON)))

    def send_text_key_value(self, key, value):
        for ele, text in [(self.send_text_key, key), (self.send_text_value, value)]:
            ele.clear()
            ele.send_keys(text)
        self.send_text_button.click()
