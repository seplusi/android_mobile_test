from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PopUp(object):

    PARENT_PANEL = 'com.example.androidsampleapp.qa:id/parentPanel'
    BUTTON_YES = 'android:id/button1'

    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, self.PARENT_PANEL)))

    def tap_yes_button(self):
        self.driver.find_element_by_id(self.BUTTON_YES).click()
