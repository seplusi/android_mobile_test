from appium import webdriver


class AppiumDriver(object):
    def __init__(self, session):
        desired_caps = session['desired_caps']
        self.driver = webdriver.Remote(f'http://localhost:{session["appium_port"]}/wd/hub', desired_caps)
