import pytest
from main.lib.appium_driver import AppiumDriver
import os
import json


@pytest.fixture(scope='function', name="driver")
def driver(session):
    driver = AppiumDriver(session).driver
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def session():
    current_path = os.path.abspath(__file__)
    for _ in range(10):
        if current_path.split('/')[-1] == 'main':
            project_path = current_path
            break
        current_path = '/'.join(current_path.split('/')[:-1])
    with open(f'{project_path}/config/session_config.json', 'r') as f:
        session = json.load(f)
    session['proj_path'] = project_path
    session['desired_caps']['app'] = f"{project_path}/{session['desired_caps']['app']}"
    yield session
