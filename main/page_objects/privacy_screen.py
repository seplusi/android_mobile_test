from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PrivacyScreen(object):

    TEXT_VIEW = 'com.example.androidsampleapp.qa:id/textView'
    FORGET_ME_BUTTON = 'com.example.androidsampleapp.qa:id/forgetme_button'
    RESUME_TRACKING = 'com.example.androidsampleapp.qa:id/resume_tracking_button'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.TEXT_VIEW)))
        self.forget_me_button = self.wait.until(EC.visibility_of_element_located((By.ID, self.FORGET_ME_BUTTON)))
        self.resume_tracking_button = self.wait.until(EC.visibility_of_element_located((By.ID, self.RESUME_TRACKING)))

    def tap_forget_me(self):
        self.forget_me_button.click()

    def tap_resume_tracking(self):
        self.resume_tracking_button.click()

