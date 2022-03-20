from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from main.page_objects.base_page import BasePage


class PrivacyScreen(BasePage):

    TEXT_VIEW = 'com.example.androidsampleapp.qa:id/textView'
    FORGET_ME_BUTTON = 'com.example.androidsampleapp.qa:id/forgetme_button'
    RESUME_TRACKING = 'com.example.androidsampleapp.qa:id/resume_tracking_button'

    def __init__(self, driver, wait_time=5):
        super(PrivacyScreen, self).__init__(driver, wait_time=wait_time)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.TEXT_VIEW)))
        self.forget_me_button = self.wait.until(EC.visibility_of_element_located((By.ID, self.FORGET_ME_BUTTON)))
        self.resume_tracking_button = self.wait.until(EC.visibility_of_element_located((By.ID, self.RESUME_TRACKING)))

    def tap_forget_me(self):
        self.forget_me_button.click()

    def tap_resume_tracking(self):
        self.resume_tracking_button.click()

