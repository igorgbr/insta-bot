from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class instaBot:
    def __init__(self, email, password, driver):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option(
            "prefs", {"intl.accept_languages": "en,en_US"}
        )
        self.driver = webdriver.Chrome(
            driver, chrome_options=self.browserProfile)
        self.email = email
        self.password = password

    def signIn(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)

        emailInput = self.driver.find_elements_by_css_selector("form input")[
            0]

        passwordInput = self.driver.find_elements_by_css_selector("form input")[
            1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def exitAndClose(self):
        self.driver.quit()
