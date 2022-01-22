from time import sleep, time
from followers import Followers
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    InvalidSessionIdException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helper import DRIVER_PATH_CHROME, DRIVER_PATH_FIREFOX, cor_terminal
from connection_driver import connection
from send_message import send_msg
from datetime import date, datetime, timedelta
from connection_banco import insert_data
from user_list import user_list
import sys
import os

# from arduino import ArduinoLeds
import requests

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

driver = webdriver.Chrome(executable_path=DRIVER_PATH_CHROME)
connection(driver)

today = date.today()
log = open(f"logs/{dir}/log - {today}", "a")

for user in user_list:
    try:
        driver.get(f"https://www.instagram.com/{user}/?hl=pt-br")
    except InvalidSessionIdException:
        print(f'{cor_terminal["red"]}TOKEN EXPIRADO{cor_terminal["clean"]}')
        log.write(f"{user} - Token expirado\n")
        sys.exit()

    # -----------------------envia msg---------------------------------------
    try:
        print(
            f'{cor_terminal["cyan"]}processando usuário: {user}{cor_terminal["clean"]}'
        )
        send_msg(user, driver)
        driver.get(f"https://www.instagram.com/{user}/")
        print("Mensagem enviada")
        sleep(1)

    except NoSuchElementException as e:
        print(e)
        pass

    except ElementClickInterceptedException as e:
        print(e)
        pass
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
            print(
                f'{cor_terminal["yellow"]}Usuario não tem postagem{cor_terminal["clean"]}'
            )

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
    for i in range(1, 10):
        driver.implicitly_wait(0.4)
        try:
            sleep(2.5)
            unlike_elements = driver.find_element(
                By.XPATH, "//*[local-name()='svg' and @aria-label='Descurtir']"
            )

            # //*[local-name()='svg' and @aria-label='Descurtir']
            print(unlike_elements)
            if not unlike_elements:
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
                            print(f"Total de likes: {tot_like}")
                            print(
                                f'excesso de requisição {timeError.strftime("%H:%M")} volta em {timeRegret.strftime("%H:%M")}'
                            )
                            sleep(300)
                            # lights.yellow_led_on()

                    except Exception:
                        ...
                    # sleep(0.5)
                    print(
                        f'{cor_terminal["green"]} post {i} - não tinha like{cor_terminal["clean"]}'
                    )
                    like += 1
                    webdriver.ActionChains(driver).key_down(
                        Keys.ARROW_RIGHT
                    ).key_up(Keys.ARROW_RIGHT).perform()
                except NoSuchElementException:
                    print("end")
                    break
            else:
                try:
                    webdriver.ActionChains(driver).key_down(
                        Keys.ARROW_RIGHT
                    ).key_up(Keys.ARROW_RIGHT).perform()
                except NoSuchElementException:
                    break

        except ElementClickInterceptedException:
            webdriver.ActionChains(driver).key_down(
                Keys.ARROW_RIGHT
            ).key_up(Keys.ARROW_RIGHT).perform()

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
        timeError = datetime.now()
        timeRegret = timeError + timedelta(seconds=900)
        print(f"Total de likes: {tot_like}")
        print(
            f'excesso de requisição {timeError.strftime("%H:%M")} volta em {timeRegret.strftime("%H:%M")}'
        )
        sleep(900)
        # lights.yellow_led_on()

    tot_like += like
    insert_data(user, like)
    # - inserir aqui

    log.write(f"{user} - Não possui mais posts\n")


# lights.yellow_led_off()
print(f'{cor_terminal["green"]} Fim do SCRIPT{cor_terminal["clean"]}')
tot_like += like
print(
    f'{cor_terminal["green"]} {len(user_list)} Usuarios varridos{cor_terminal["clean"]}'
)
print(
    f'{cor_terminal["green"]} Total de likes: {tot_like}{cor_terminal["clean"]}'
)
# lights.blue_led_blink()
driver.close()
sys.exit()
