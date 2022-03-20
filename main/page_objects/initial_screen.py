import time
from main.lib.actions import Action
from main.lib.utils import compare_2_images
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from main.page_objects.base_page import BasePage


class InitialScreen(BasePage):

    TOOLBAR = 'com.example.androidsampleapp.qa:id/toolbar'
    APP_ID = 'com.example.androidsampleapp.qa:id/label_'
    APP_FULL_SCREEN = 'android:id/content'
    PRIVACY = 'com.example.androidsampleapp.qa:id/label_privacy'
    FRAGMENT = 'com.example.androidsampleapp.qa:id/label_fragment'
    POPUP = 'com.example.androidsampleapp.qa:id/label_popup'
    DYNAMIC = 'com.example.androidsampleapp.qa:id/label_dynamic_variables'

    def __init__(self, driver, wait_time=5):
        super(InitialScreen, self).__init__(driver, wait_time=wait_time)
        self.toolbar = self.wait.until(EC.visibility_of_element_located((By.ID, self.TOOLBAR)))
        self.title = self.toolbar.find_element_by_class_name('android.widget.TextView')
        self.fragment_btn = self.wait.until(EC.element_to_be_clickable((By.ID, self.FRAGMENT)))
        self.popup_btn = self.wait.until(EC.element_to_be_clickable((By.ID, self.POPUP)))
        self.dynamic = self.wait.until(EC.element_to_be_clickable((By.ID, self.DYNAMIC)))

    def long_press(self, duration):
        duration = duration*1000
        Action(self.driver).long_press(self.title, duration)

    def tap_fragment(self):
        self.fragment_btn.click()

    def tap_privacy(self):
        Action(self.driver).swipe_up()
        self.privacy_btn = self.wait.until(EC.element_to_be_clickable((By.ID, self.PRIVACY)))
        self.privacy_btn.click()

    def tap_popup(self):
        self.popup_btn.click()

    def tap_dynamic_variables(self):
        self.dynamic.click()

    def verify_toast_is_shown(self, proj_path, udid, timeout=10):
        org_file = f"{proj_path}/binaries/images/{udid}/initial_screen_red.png"
        dest_file = f'{proj_path}/output/initial_screen_red_{udid}.png'
        for i in range(timeout):
            with open(dest_file, "wb") as f:
                f.write(self.driver.find_element_by_id(self.APP_FULL_SCREEN).screenshot_as_png)
            if compare_2_images(org_file, dest_file):
                break
            time.sleep(1)
        else:
            raise TimeoutError(f'Image {proj_path}/binaries/images/{udid}/initial_screen_red.png was not found')
