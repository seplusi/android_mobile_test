from main.lib.actions import Action
from main.lib.utils import compare_2_images
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import cv2
import time


class InitialScreen(object):

    TOOLBAR = 'com.example.androidsampleapp.qa:id/toolbar'
    APP_ID = 'com.example.androidsampleapp.qa:id/label_'
    APP_FULL_SCREEN = 'android:id/content'

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.toolbar = self.wait.until(EC.visibility_of_element_located((By.ID, self.TOOLBAR)))
        self.title = self.toolbar.find_element_by_class_name('android.widget.TextView')

    def long_press(self, duration):
        duration = duration*1000
        Action(self.driver).long_press(self.title, duration)

    def tap_track(self, ele_text):
        ele_text = ele_text.lower().replace(' ', '_')
        selector = f'{self.APP_ID}{ele_text.lower()}'
        self.driver.find_element_by_id(selector).click()

    def verify_toast_is_shown(self, proj_path, timeout=10):
        org_file = f"{proj_path}/binaries/images/initial_screen_red.png"
        dest_file = f'{proj_path}/output/initial_screen_red.png'
        for i in range(timeout):
            with open(dest_file, "wb") as f:
                f.write(self.driver.find_element_by_id(self.APP_FULL_SCREEN).screenshot_as_png)
            if compare_2_images(org_file, dest_file):
                break
            time.sleep(1)
        else:
            raise TimeoutError(f'Image {proj_path}/binaries/images/initial_screen_red.png was not found')
