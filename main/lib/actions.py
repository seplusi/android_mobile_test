import time
from appium.webdriver.common.touch_action import TouchAction


class Action(object):
    def __init__(self, driver):
        self.driver = driver
        self.screen_dimensions = self.driver.get_window_size()

    def long_press(self, element, duration):
        actions = TouchAction(self.driver)
        actions.long_press(element, duration=duration)
        actions.perform()

    def swipe_left(self, duration=500):
        startx = self.screen_dimensions['width']*0.9
        endx = self.screen_dimensions['width']*0.2
        starty = self.screen_dimensions['height']/2
        endy = self.screen_dimensions['height']/2
        self.driver.swipe(startx, starty, endx, endy, duration)

    def swipe_up(self, duration=500):
        startx = self.screen_dimensions['width'] / 2
        endx = self.screen_dimensions['width'] / 2
        starty = self.screen_dimensions['height'] * 0.9
        endy = self.screen_dimensions['height'] * 0.3
        self.driver.swipe(startx, starty, endx, endy, duration)

    def go_back(self):
        self.driver.back()

    def place_app_background(self, duration):
        self.driver.background_app(duration)

    def kill_app(self):
        self.driver.terminate_app(self.driver.current_package)

    def close_app(self):
        self.driver.close_app()

    def restart_app(self):
        self.driver.reset()

    def wait_for_app_to_state(self, state, package, timeout=5):
        for _ in range(timeout):
            if self.driver.query_app_state(package) == state:
                break
            time.sleep(1)
        else:
            raise TimeoutError(f'Could not find package {package} with running status {state}')
