from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from helper import DRIVER_PATH_CHROME, cor_terminal
from connection import connection
from send_message import send_msg
from datetime import date
from connectionBanco import insert_data

driver = webdriver.Chrome(
    executable_path=DRIVER_PATH_CHROME)
connection(driver)

# ----------------------------------------------------------------------
# hashtag = 'tecnologia'
# driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')

user = 'gswdatabook'
driver.get(f'https://www.instagram.com/{user}/?hl=pt-br')

# -----------------------envia msg---------------------------------------
# try:
#     send_msg(user, driver)
#     driver.get(f'https://www.instagram.com/{user}/')
# except NoSuchElementException:
#     pass
# ----------------------------------------------------------------------

driver.find_element_by_class_name('_9AhH0').click()  # - Clicka na imagem

# ------------------------ like posts -----------------------------------------
today = date.today()
for i in range(1, 400):
    driver.implicitly_wait(0.4)
    try:
        unlike_elements = driver.find_elements_by_css_selector(
            "[aria-label='Descurtir']")
        if not unlike_elements:
            try:
                driver.find_element_by_class_name('fr66n').click()
                print(
                    f'{cor_terminal["green"]} post {i} - não tinha like{cor_terminal["clean"]}')
                driver.find_element_by_class_name('_65Bje').click()
            except NoSuchElementException:
                print("end")
                insert_data(user, i)
                driver.close()
                break
        else:
            try:
                driver.find_element_by_class_name('_65Bje').click()
            except NoSuchElementException:
                insert_data(user, i)
                driver.close()
                break

    except ElementClickInterceptedException:
        driver.find_element_by_class_name('_65Bje').click()
