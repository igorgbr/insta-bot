import sys
import os
import requests
import random

from time import sleep
from followers import Followers

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    InvalidSessionIdException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from helper import DRIVER_PATH_CHROME
from connection_driver import connection

# from send_message import send_msg
from datetime import date, datetime, timedelta
from connection_banco import insert_data
from user_list import user_list

sys.path.insert(0, "helper/cli")
from CLI import (
    PROCESSANDO_USUARIO,
    TOKEN_EXPIRADO,
    USUARIO_N_TEM_POSTAGEM,
    POST_N_TEM_LIKE,
    FIM_DO_SCRIPT,
    USUARIOS_VARRIDOS,
    TOTAL_LIKES,
    EXCESSO_DE_REQUISICOES,
)

# from arduino import ArduinoLeds


# lights = ArduinoLeds()

# lights.yellow_led_on()
# ----------------------------------------------------------------------
# hashtag = 'tecnologia'
# driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')

dir = f"{date.today()}"
tot_like = 0
try:
    os.mkdir(f"logs/{dir}")
except FileExistsError:
    pass

s = Service(DRIVER_PATH_CHROME)

driver = webdriver.Chrome(service=s)
connection(driver)

today = date.today()
log = open(f"logs/{dir}/log - {today}", "a")

for user in user_list:
    try:
        PROCESSANDO_USUARIO(user)
        driver.get(f"https://www.instagram.com/{user}/?hl=pt-br")
    except InvalidSessionIdException:
        TOKEN_EXPIRADO()
        log.write(f"{user} - Token expirado\n")
        sys.exit()

    # -----------------------envia msg---------------------------------------
    # try:
    #     PROCESSANDO_USUARIO(user)
    #     # send_msg(user, driver)
    #     driver.get(f"https://www.instagram.com/{user}/")
    #     sleep(1)

    # except NoSuchElementException as e:
    #     print(e)
    #     pass

    # except ElementClickInterceptedException as e:
    #     print(e)
    #     pass
    # ----------------------------------------------------------------------
    follow = Followers(driver)
    try:
        url = driver.find_element(
            By.CSS_SELECTOR, "div div div div a"
        ).get_attribute("href")
        print(url)

        try:
            response = requests.get(url)
            # sleep(0.5)
            print(response.status_code)
        except requests.exceptions.MissingSchema:
            driver.refresh()

        if "https://www.instagram.com/p/" not in url:
            USUARIO_N_TEM_POSTAGEM()

        driver.find_element(
            By.CLASS_NAME, "_9AhH0"
        ).click()  # - Clicka na imagem

        # sleep(3)
        # response.raise_for_status()
    except NoSuchElementException:
        pass
    # except requests.HTTPError:
    #     print('excesso de requisição')
    #     driver.close()
    #     sys.exit()

    # ------------------------ like posts ----------------------------------
    like = 0

    for i in range(1, random.randint(2, 9)):
        driver.implicitly_wait(0.4)
        sleep(2.5)

        try:
            unlike_elements = driver.find_element(
                By.XPATH, "//*[local-name()='svg' and @aria-label='Descurtir']"
            )

            webdriver.ActionChains(driver).key_down(Keys.ARROW_RIGHT).key_up(
                Keys.ARROW_RIGHT
            ).perform()

        # //*[local-name()='svg' and @aria-label='Descurtir']

        except NoSuchElementException:
            try:
                like_label = driver.find_element(By.CLASS_NAME, "fr66n")
                like_label.click()
                # driver.find_element_by_css_selector("[aria-label='Curtir']").click()
                # driver.find_element_by_css_selector("[aria-label='Avançar']").click()
                try:
                    # excess_error = driver.find_element_by_class_name(
                    #     "gxNyb"
                    # ).text
                    excess_error = driver.find_element(
                        By.CLASS_NAME, "gxNyb"
                    ).text
                    print(excess_error)
                    if excess_error:
                        # lights.yellow_led_off()
                        # lights.blue_led_blink()
                        timeError = datetime.now()
                        timeRegret = timeError + timedelta(seconds=300)
                        TOTAL_LIKES(tot_like)

                        EXCESSO_DE_REQUISICOES(timeError, timeRegret)
                        sleep(300)
                        # lights.yellow_led_on()

                except Exception:
                    ...
                # sleep(0.5)
                POST_N_TEM_LIKE(i)

                like += 1
                webdriver.ActionChains(driver).key_down(
                    Keys.ARROW_RIGHT
                ).key_up(Keys.ARROW_RIGHT).perform()
            except NoSuchElementException:
                print("end")
                break

    seguindo = driver.find_elements_by_css_selector("[aria-label='Seguindo']")
    if "/p/" not in url and not seguindo:
        try:
            if (
                driver.find_element_by_class_name("rkEop").text
                == "Esta conta é privada"
            ):
                follow.follow(1)
        except NoSuchElementException:
            try:
                if (
                    driver.find_element_by_tag_name("h2").text
                    == "Esta página não está disponível."
                ):
                    pass
                else:
                    follow.follow(0)
            except:
                pass

    if "/p/" in url and like == 0 and not unlike_elements:
        # lights.yellow_led_off()
        # lights.blue_led_blink()
        TOTAL_LIKES(tot_like)

        timeError = datetime.now()
        timeRegret = timeError + timedelta(seconds=900)
        EXCESSO_DE_REQUISICOES(timeError, timeRegret)
        sleep(900)
        # lights.yellow_led_on()

    tot_like += like
    insert_data(user, like)
    # - inserir aqui

    log.write(f"{user} - Não possui mais posts\n")


# lights.yellow_led_off()
FIM_DO_SCRIPT()
tot_like += like

USUARIOS_VARRIDOS(user_list)
TOTAL_LIKES(tot_like)
# lights.blue_led_blink()
driver.close()
sys.exit()
