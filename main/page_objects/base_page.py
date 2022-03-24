from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, driver, wait_time=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)
