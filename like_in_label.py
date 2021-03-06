from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from helper import DRIVER_PATH_CHROME, DRIVER_PATH_FIREFOX, cor_terminal
from connection_driver import connection
from datetime import date
from send_message import send_msg
from time import sleep
from connection_banco import insert_data
import sys
from arduino import ArduinoLeds

lights = ArduinoLeds()

lights.yellow_led_on()
# -------------------------------------LOGIN---------------------------------------
driver = webdriver.Chrome(
    executable_path=DRIVER_PATH_CHROME)
connection(driver)

# ----------------------------------------------------------------------
user = 'ga.brielapinheiro'
driver.get(f'https://www.instagram.com/{user}/')

try:
    send_msg(user, driver)
    driver.get(f'https://www.instagram.com/{user}/')
except NoSuchElementException:
    pass

driver.find_element_by_class_name('_9AhH0').click()  # - Clicka na imagem

driver.implicitly_wait(0.5)
# ------------------------ like comments and posts ----------------------------
total_count = 0
today = date.today()
for i in range(1, 20):
    like_elements = driver.find_elements_by_css_selector(
        "[aria-label='Curtir']")

    if not like_elements:
        print(
            f'{cor_terminal["red"]}post {i} - já tem like{cor_terminal["clean"]}')

        try:
            next_button = driver.find_element_by_class_name('_65Bje')
            next_button.click()
        except NoSuchElementException:
            insert_data(user, i, total_count)
            driver.find_element_by_css_selector(
                "[aria-label='Fechar']").click()
            driver.quit()
            sys.exit()

        except ElementClickInterceptedException:
            insert_data(user, i, total_count)
            driver.quit()
            sys.exit()

    else:
        print(
            f'{cor_terminal["green"]} post {i} - não tinha like{cor_terminal["clean"]}')
        count = 1
        for like in like_elements:
            try:
                like.click()  # - Clicka no like
                print(
                    f'{cor_terminal["cyan"]}{count} likes dentro do post {i}{cor_terminal["clean"]}')
                count += 1
                total_count += count
            except ElementClickInterceptedException:

                insert_data(user, i, total_count)
                driver.quit()
                sys.exit()
        try:
            next_button = driver.find_element_by_class_name('_65Bje')
            next_button.click()
        except NoSuchElementException:
            insert_data(user, i, total_count)
            print(
                f'{cor_terminal["red"]}Não possui mais posts!{cor_terminal["clean"]}')
            driver.quit()
            sys.exit()
        except ElementClickInterceptedException:
            insert_data(user, i, total_count)
            driver.quit()
            sys.exit
insert_data(user, i, total_count)
driver.quit()
lights.yellow_led_off()
print(f'{cor_terminal["green"]} Fim do SCRIPT{cor_terminal["clean"]}')
lights.blue_led_blink()

# ----- recebe um lista com a classe das imagens -------------
# lista_imagens = driver.find_elements_by_class_name('_9AhH0')
# print(lista_imagens)
