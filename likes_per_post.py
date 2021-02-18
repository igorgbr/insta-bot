from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from helper import DRIVER_PATH, cor_terminal
from connection import connection

driver = webdriver.Chrome(
    executable_path=DRIVER_PATH)
connection(driver)

# ----------------------------------------------------------------------
driver.get('https://www.instagram.com/explore/tags/programação/')
driver.find_element_by_class_name('_9AhH0').click()  # - Clicka na imagem


driver.implicitly_wait(1)
# ------------------------ like posts -----------------------------------------
for i in range(1, 400):
    try:
        unlike_elements = driver.find_elements_by_css_selector(
            "[aria-label='Descurtir']")
        if not unlike_elements:
            driver.find_element_by_xpath(
                "//span[@class='fr66n']").click()
            print(
                f'{cor_terminal["green"]} post {i} - não tinha like{cor_terminal["clean"]}')
            driver.find_element_by_class_name('_65Bje').click()
        else:
            driver.find_element_by_class_name('_65Bje').click()
    except ElementClickInterceptedException:
        driver.find_element_by_class_name('_65Bje').click()
