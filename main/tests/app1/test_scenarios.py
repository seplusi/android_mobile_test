import pytest
from main.page_objects.initial_screen import InitialScreen
from main.page_objects.fragment_screen import FragmentScreen
from main.page_objects.popup import PopUp
from main.lib.actions import Action
from main.page_objects.dynamic_values_screen import DynamicValuesScreen
from main.page_objects.privacy_screen import PrivacyScreen
from selenium.common.exceptions import TimeoutException


@pytest.mark.scenarios
class TestScenarios(object):

    def test_scenario1(self, session, driver):
        ini_screen = InitialScreen(driver)
        ini_screen.long_press(2)
        ini_screen.tap_track('Fragment')

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
        ini_screen.tap_track("Popup")

        PopUp(driver).tap_yes_button()
        InitialScreen(driver).verify_toast_is_shown(session['proj_path'])

        # Place app in background. Bring back, close it and verify status
        Action(driver).place_app_background(2)
        InitialScreen(driver)
        Action(driver).close_app()
        Action(driver).wait_for_app_to_state(1, session['app_package'])

    def test_scenario2(self, session, driver):
        ini_screen = InitialScreen(driver)
        ini_screen.tap_track('Dynamic Variables')

        dyn_screen = DynamicValuesScreen(driver)
        dyn_screen.send_text_key_value('test', '1234')
        Action(driver).go_back()

        InitialScreen(driver).tap_track('Privacy')

        PrivacyScreen(driver).tap_forget_me()

        Action(driver).kill_app()
        with pytest.raises(TimeoutException):
            InitialScreen(driver, 1)

        Action(driver).restart_app()
        InitialScreen(driver).tap_track('Privacy')
        PrivacyScreen(driver).tap_resume_tracking()
        Action(driver).go_back()
        InitialScreen(driver)
        Action(driver).close_app()

        Action(driver).wait_for_app_to_state(1, session['app_package'])
        driver.query_app_state(driver.current_package)
