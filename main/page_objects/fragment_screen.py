from main.page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FragmentScreen(BasePage):

    ACTIONBAR = 'com.example.androidsampleapp.qa:id/action_bar'
    TABS = 'com.example.androidsampleapp.qa:id/tabs'
    FIRST_TAB = 'First Tab'
    SECOND_TAB = 'Second Tab'
    THIRD_TAB = 'Third Tab'
    FRAGMENT_TEXT = 'com.example.androidsampleapp.qa:id/fragment_text'

    def __init__(self, driver, fragment_text, wait_time=5):
        super(FragmentScreen, self).__init__(driver, wait_time=wait_time)
        self.actionbar = self.wait.until(EC.visibility_of_element_located((By.ID, self.ACTIONBAR)))
        self.wait.until(EC.text_to_be_present_in_element((By.ID, self.FRAGMENT_TEXT), fragment_text))
        self.title = self.actionbar.find_element_by_class_name('android.widget.TextView')
        self.first_tab = self.driver.find_element_by_accessibility_id(self.FIRST_TAB)
        self.second_tab = self.driver.find_element_by_accessibility_id(self.SECOND_TAB)
        self.third_tab = self.driver.find_element_by_accessibility_id(self.THIRD_TAB)

    def tab_selected_value(self, tab_name):
        if tab_name == 'FIRST TAB':
            value = self.first_tab.get_attribute('selected')
        elif tab_name == 'SECOND TAB':
            value = self.second_tab.get_attribute('selected')
        else:
            value = self.third_tab.get_attribute('selected')

        return value

    def tap_tab(self, tab_name):
        if tab_name == 'FIRST TAB':
            self.first_tab.click()
        elif tab_name == 'SECOND TAB':
            self.second_tab.click()
        else:
            self.third_tab.click()

    def get_fragment_text(self):
        return self.driver.find_element_by_id(self.FRAGMENT_TEXT).text
