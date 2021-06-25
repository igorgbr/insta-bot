from selenium.webdriver.common.keys import Keys
from helper import PASSWORD, LOGIN
import requests
import time
import sys


def connection(driver):
    try:
        # response = requests.get("http://www.instagram.com.br", timeout=3)
        # time.sleep(0.5)
        # print(response.status_code)
        # response.raise_for_status()
        driver.get("http://www.instagram.com.br")

        driver.implicitly_wait(5)
        driver.find_element_by_name('username').send_keys(LOGIN)
        driver.find_element_by_name('password').send_keys(PASSWORD)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)

        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='Agora não']").click()

        driver.find_element_by_xpath("//button[text()='Agora não']").click()
        driver.find_element_by_class_name('cq2ai').click()
    except requests.HTTPError:
        print('excesso de requisição!')
        driver.close()
        sys.exit()
