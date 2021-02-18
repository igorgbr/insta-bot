from selenium.webdriver.common.keys import Keys
from helper import PASSWORD, LOGIN


def connection(driver):
    driver.get("http://www.instagram.com.br")

    driver.implicitly_wait(3)
    driver.find_element_by_name('username').send_keys(LOGIN)
    driver.find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_name('password').send_keys(Keys.RETURN)

    driver.find_element_by_xpath("//button[text()='Agora não']").click()
    driver.find_element_by_class_name('cq2ai').click()
