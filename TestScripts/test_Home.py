import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.HomePage import HomePage1


class TestHome:

    @pytest.fixture
    def setup(self):
        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.implicitly_wait(10)

        yield driver
        driver.quit()

    def test_login(self, setup):
        home = HomePage1(setup)
        assert home.login() == True
        print("SUCCESS: Logged In (Positive)")

    def test_invalid_login(self, setup):
        home = HomePage1(setup)
        assert home.invalid_login() == True
        print("SUCCESS: Not Logged In (Negative)")

    def test_logout(self, setup):
        home = HomePage1(setup)
        home.login()
        home.logout()
        print("SUCCESS: Logged out")
