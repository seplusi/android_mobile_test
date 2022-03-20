from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from main.page_objects.base_page import BasePage


class PopUp(BasePage):

    PARENT_PANEL = 'com.example.androidsampleapp.qa:id/parentPanel'
    BUTTON_YES = 'android:id/button1'

    def __init__(self, driver, wait_time=5):
        super(PopUp, self).__init__(driver, wait_time=wait_time)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.PARENT_PANEL)))

    def tap_yes_button(self):
        self.driver.find_element_by_id(self.BUTTON_YES).click()
