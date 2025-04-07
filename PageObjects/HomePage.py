from selenium.webdriver.common.by import By
from TestData.data import ZenData
from TestLocators.locators import ZenLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
class HomePage1:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get(ZenData.Zen_url)
        self.driver.find_element(by=By.ID, value=ZenLocators.username_locator).send_keys(ZenData.username)
        self.driver.find_element(by=By.ID, value=ZenLocators.password_locator).send_keys(ZenData.password)
        self.driver.find_element(by=By.XPATH, value=ZenLocators.login_button_locator).click()
        self.driver.implicitly_wait(5)
        try:
            close_button = self.driver.find_element(By.XPATH, "//button[@class='custom-close-button']")
            close_button.click()
            print("INFO: Closed the popup using close button.")
        except NoSuchElementException:
            print("INFO: No popup appeared, continuing normally.")

        return True

        return True

    def invalid_login(self):
        self.driver.get(ZenData.Zen_url)
        self.driver.find_element(by=By.ID, value=ZenLocators.username_locator).send_keys(ZenData.invalid_username)
        self.driver.find_element(by=By.ID, value=ZenLocators.password_locator).send_keys(ZenData.invalid_password)
        self.driver.find_element(by=By.XPATH, value=ZenLocators.login_button_locator).click()
        return True

    def logout(self):
        self.driver.find_element(by=By.XPATH, value=ZenLocators.profile_id_click).click()
        self.driver.find_element(by=By.XPATH, value=ZenLocators.logout_button_locator).click()
        return self.driver.current_url
