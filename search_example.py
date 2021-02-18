from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import DRIVER_PATH
from connection import connection

# -------------------------------------LOGIN---------------------------------------
driver = webdriver.Chrome(
    executable_path=DRIVER_PATH)
connection(driver)

# ---------------------------------LIKES-------------------------------------------
i = 0
for y in range(50):
    driver.implicitly_wait(1000)
    element = driver.find_elements_by_css_selector("[aria-label='Curtir']")
    for x in element:
        print(f'like {i}')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[aria-label='Curtir']"))).click()
        i += 1
    driver.implicitly_wait(2000)
