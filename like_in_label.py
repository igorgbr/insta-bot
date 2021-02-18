from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from helper import DRIVER_PATH, cor_terminal
from connection import connection

# -------------------------------------LOGIN---------------------------------------
driver = webdriver.Chrome(
    executable_path=DRIVER_PATH)
connection(driver)

# ----------------------------------------------------------------------
user = 'matheusfc.dev'
driver.get(f'https://www.instagram.com/{user}/')
driver.find_element_by_class_name('_9AhH0').click()  # - Clicka na imagem


driver.implicitly_wait(0.5)

# ------------------------ like comments and posts ----------------------------
for i in range(1, 50):
    like_elements = driver.find_elements_by_css_selector(
        "[aria-label='Curtir']")

    if not like_elements:
        print(
            f'{cor_terminal["red"]}post {i} - tem like{cor_terminal["clean"]}')

        try:
            next_button = driver.find_element_by_class_name('_65Bje')
            next_button.click()
        except NoSuchElementException:
            print("end")
            driver.find_element_by_css_selector(
                "[aria-label='Fechar']").click()
            driver.quit()
            break

    else:
        print(
            f'{cor_terminal["green"]} post {i} - não tinha like{cor_terminal["clean"]}')
        count = 1
        for like in like_elements:
            like.click()
            print(
                f'{cor_terminal["cyan"]}{count} likes dentro do post {i}{cor_terminal["clean"]}')
            count += 1

        try:
            next_button = driver.find_element_by_class_name('_65Bje')
            next_button.click()
        except NoSuchElementException:
            print("end")
            driver.find_element_by_css_selector(
                "[aria-label='Fechar']").click()
            driver.quit()
            break



# ----- recebe um lista com a classe das imagens -------------
# lista_imagens = driver.find_elements_by_class_name('_9AhH0')
# print(lista_imagens)
