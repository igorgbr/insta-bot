from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data_login import PASSWORD, LOGIN, DRIVER_PATH

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
driver.get('https://www.instagram.com/velocidadecode/')

driver.find_element_by_class_name('_9AhH0').click()  # - Clicka na imagem

# ----- recebe um lista com a classe das imagens -------------
# lista_imagens = driver.find_elements_by_class_name('_9AhH0')
# print(lista_imagens)
driver.implicitly_wait(0.5)
for i in range(50):
    like_elements = driver.find_elements_by_css_selector(
        "[aria-label='Curtir']")

    if not like_elements:
        print(f'post {i} - tem like')
        driver.find_element_by_class_name('_65Bje').click()
    else:
        print(f'post {i} - não tinha like')
        count = 0
        for like in like_elements:
            like.click()
            print(f'{count} - likes dentro do post {i}')
            count += 1

        driver.find_element_by_class_name('_65Bje').click()
