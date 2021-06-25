from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, InvalidSessionIdException
from helper import DRIVER_PATH_CHROME, DRIVER_PATH_FIREFOX, cor_terminal
from connection_driver import connection
from send_message import send_msg
from datetime import date
from connection_banco import insert_data
from user_list import user_list
import sys
import os
from arduino import ArduinoLeds
import requests

lights = ArduinoLeds()

lights.yellow_led_on()
# ----------------------------------------------------------------------
# hashtag = 'tecnologia'
# driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')

dir = f'{date.today()}'

try:
    os.mkdir(f'logs/{dir}')
except FileExistsError:
    pass

driver = webdriver.Chrome(
    executable_path=DRIVER_PATH_CHROME)
connection(driver)

today = date.today()
log = open(f'logs/{dir}/log - {today}', 'a')

totalWarning = 0


def verifyWarning(totalWarning):
    print(totalWarning)
    if totalWarning > 3:
        print(
            f'{cor_terminal["yellow"]}WARNING: {totalWarning}{cor_terminal["clean"]}')
    if(totalWarning > 7):
        print(
            f'{cor_terminal["red"]}ERROR: Excesso de Warnings: {totalWarning}{cor_terminal["clean"]}')
        lights.yellow_led_off()
        print(f'{cor_terminal["green"]} Fim do SCRIPT{cor_terminal["clean"]}')
        lights.blue_led_blink()
        driver.close()
        sys.exit()


for user in user_list:
    try:
        driver.get(f'https://www.instagram.com/{user}/?hl=pt-br')
    except InvalidSessionIdException:
        print(f'{cor_terminal["red"]}TOKEN EXPIRADO{cor_terminal["clean"]}')
        log.write(f'{user} - Token expirado\n')
        sys.exit()

    # -----------------------envia msg---------------------------------------
    # try:
    #     send_msg(user, driver)
    #     driver.get(f'https://www.instagram.com/{user}/')
    #     print('Mensagem enviada')
    # except NoSuchElementException:
    #     pass
    # ----------------------------------------------------------------------
    try:
        url = driver.find_element_by_css_selector(
            'div div div div a').get_attribute('href')
        print(url)
        # response = requests.get(url)
        # sleep(0.5)
        # print(response.status_code)

        driver.find_element_by_class_name(
            '_9AhH0').click()  # - Clicka na imagem
        sleep(1)
        # response.raise_for_status()
    except NoSuchElementException:
        pass
    except requests.HTTPError:
        print('excesso de requisição')
        driver.close()
        sys.exit()

    # ------------------------ like posts ----------------------------------
    for i in range(1, 30):
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
                    break
            else:
                try:
                    driver.find_element_by_class_name('_65Bje').click()
                except NoSuchElementException:
                    break

        except ElementClickInterceptedException:
            driver.find_element_by_class_name('_65Bje').click()

    insert_data(user, i)
    # - inserir aqui
    if(i == 1):
        totalWarning += 1

    # verifyWarning(totalWarning)

    log.write(f'{user} - Não possui mais posts\n')


lights.yellow_led_off()
print(f'{cor_terminal["green"]} Fim do SCRIPT{cor_terminal["clean"]}')
lights.blue_led_blink()
driver.close()
sys.exit()
