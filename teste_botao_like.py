from selenium import webdriver
from helper import DRIVER_PATH_FIREFOX, DRIVER_PATH_CHROME
from connection_driver import connection

driver = webdriver.Firefox(
    executable_path=DRIVER_PATH_CHROME)
connection(driver)

driver.get(f'https://www.instagram.com/luanprates/?hl=pt-br')

driver.find_element_by_class_name('_9AhH0').click()
