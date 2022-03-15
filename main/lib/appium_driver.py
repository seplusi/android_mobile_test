from appium import webdriver


class AppiumDriver(object):
    def __init__(self, session):
        desired_caps = session['desired_caps']
#        desired_caps['app'] = f'{session["proj_path"]}/{desired_caps["app"]}'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
