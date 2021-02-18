from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from helper import DRIVER_PATH, cor_terminal
from connection import connection
from datetime import date


# -------------------------------------LOGIN---------------------------------------
driver = webdriver.Chrome(
    executable_path=DRIVER_PATH)
connection(driver)

# ----------------------------------------------------------------------
user = 'tiagoandrade_pe'
f = open(f"data/{user}.txt", "a")
driver.get(f'https://www.instagram.com/{user}/')
driver.find_element_by_class_name('_9AhH0').click()  # - Clicka na imagem


driver.implicitly_wait(0.5)
# ------------------------ like comments and posts ----------------------------
total_count = 0
today = date.today()
for i in range(1, 50):
    like_elements = driver.find_elements_by_css_selector(
        "[aria-label='Curtir']")

    if not like_elements:
        print(
            f'{cor_terminal["red"]}post {i} - já tem like{cor_terminal["clean"]}')

        try:
            next_button = driver.find_element_by_class_name('_65Bje')
            next_button.click()
        except NoSuchElementException:
            print("end")
            f.write(
                f"{user} - total posts: {i} || total likes: {total_count} || Date: {today}")
            f.close()
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
            total_count += count
        try:
            next_button = driver.find_element_by_class_name('_65Bje')
            next_button.click()
        except NoSuchElementException:
            print("end")
            f.write(
                f"{user} - total posts: {i} || total likes: {total_count} || Date: {today}")
            f.close()

            driver.find_element_by_css_selector(
                "[aria-label='Fechar']").click()
            driver.quit()
            break

f.write(f"{user} - total posts: {i} || total likes: {total_count} || Date: {today}")
f.close()


# ----- recebe um lista com a classe das imagens -------------
# lista_imagens = driver.find_elements_by_class_name('_9AhH0')
# print(lista_imagens)
