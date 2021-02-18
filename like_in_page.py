from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from helper import PASSWORD, LOGIN, DRIVER_PATH, cor_terminal

# -------------------------------------LOGIN---------------------------------------
driver = webdriver.Chrome(
    executable_path=DRIVER_PATH)
driver.get("http://www.instagram.com.br")

driver.implicitly_wait(3)
driver.find_element_by_name('username').send_keys(LOGIN)
driver.find_element_by_name('password').send_keys(PASSWORD)
driver.find_element_by_name('password').send_keys(Keys.RETURN)


driver.find_element_by_xpath("//button[text()='Agora não']").click()
driver.find_element_by_class_name('cq2ai').click()

# ----------------------------------------------------------------------
driver.get('https://www.instagram.com/ocodetop/')

driver.find_element_by_class_name('_9AhH0').click()  # - Clicka na imagem

# ----- recebe um lista com a classe das imagens -------------
# lista_imagens = driver.find_elements_by_class_name('_9AhH0')
# print(lista_imagens)
driver.implicitly_wait(1)
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
