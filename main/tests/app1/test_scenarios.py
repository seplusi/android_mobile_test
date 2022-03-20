import pytest
import os
import json
from main.page_objects.initial_screen import InitialScreen
from main.page_objects.fragment_screen import FragmentScreen
from main.page_objects.popup import PopUp
from main.lib.actions import Action
from main.lib.appium_driver import AppiumDriver
from main.page_objects.dynamic_values_screen import DynamicValuesScreen
from main.page_objects.privacy_screen import PrivacyScreen
from selenium.common.exceptions import TimeoutException


def get_driver(udid, systemPort, appPort, platformVersion):
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
    session['desired_caps']['udid'] = udid
    session['desired_caps']['systemPort'] = systemPort
    session['desired_caps']['platformVersion'] = platformVersion
    session['appium_port'] = appPort

    driver = AppiumDriver(session).driver

    return driver, session


@pytest.mark.parametrize("udid, platformVersion, systemPort, appPort", [('emulator-5554', '10', '8201', 4723), ('emulator-5556', '11', '8202', 4724)])
def test_scenario1(udid, platformVersion, systemPort, appPort):

    driver, session = get_driver(udid, systemPort, appPort, platformVersion)

    ini_screen = InitialScreen(driver)
    ini_screen.long_press(2)
    ini_screen.tap_fragment()

    frag_screen = FragmentScreen(driver, 'First Fragment')
    assert frag_screen.tab_selected_value('FIRST TAB') == 'true'
    assert frag_screen.get_fragment_text() == 'First Fragment'
    Action(driver).swipe_left()

    frag_screen = FragmentScreen(driver, 'Second Fragment')
    assert frag_screen.tab_selected_value('SECOND TAB') == 'true'
    assert frag_screen.get_fragment_text() == 'Second Fragment'
    frag_screen.tap_tab('FIRST TAB')

    frag_screen = FragmentScreen(driver, 'First Fragment')
    assert frag_screen.tab_selected_value('FIRST TAB') == 'true'
    assert frag_screen.get_fragment_text() == 'First Fragment'

    Action(driver).go_back()
    ini_screen = InitialScreen(driver)
    ini_screen.tap_popup()

    PopUp(driver).tap_yes_button()
    InitialScreen(driver).verify_toast_is_shown(session['proj_path'], session['desired_caps']['udid'])

    # Place app in background. Bring back, close it and verify status
    Action(driver).place_app_background(2)
    InitialScreen(driver)
    Action(driver).close_app()
    Action(driver).wait_for_app_to_state(1, session['app_package'])

    driver.quit()


@pytest.mark.parametrize("udid, platformVersion, systemPort, appPort", [('emulator-5554', '10', '8201', 4723), ('emulator-5556', '11', '8202', 4724)])
def test_scenario2(udid, platformVersion, systemPort, appPort):
    driver, session = get_driver(udid, systemPort, appPort, platformVersion)

    ini_screen = InitialScreen(driver)
    ini_screen.tap_dynamic_variables()

    dyn_screen = DynamicValuesScreen(driver)
    dyn_screen.send_text_key_value('test', '1234')
    Action(driver).go_back()

    InitialScreen(driver).tap_privacy()

    PrivacyScreen(driver).tap_forget_me()

    Action(driver).kill_app()
    with pytest.raises(TimeoutException):
        InitialScreen(driver, 1)

    Action(driver).restart_app()
    InitialScreen(driver).tap_privacy()
    PrivacyScreen(driver).tap_resume_tracking()
    Action(driver).go_back()
    InitialScreen(driver)
    Action(driver).close_app()

    Action(driver).wait_for_app_to_state(1, session['app_package'])
    driver.query_app_state(driver.current_package)
    driver.quit()
