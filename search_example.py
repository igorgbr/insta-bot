from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_login import PASSWORD, LOGIN, DRIVER_PATH

# -------------------------------------LOGIN---------------------------------------
driver = webdriver.Chrome(
    executable_path=DRIVER_PATH)
driver.get("http://www.instagram.com.br")
driver.implicitly_wait(10)

elem_user = driver.find_element_by_name('username')
elem_user.clear()
elem_user.send_keys(LOGIN)

elem_pass = driver.find_element_by_name('password')
elem_pass.clear()
elem_pass.send_keys(PASSWORD)

elem_user.send_keys(Keys.RETURN)
driver.implicitly_wait(30000)

element = driver.find_element_by_xpath("//button[text()='Agora não']")
element.click()

driver.find_element_by_class_name('cq2ai').click()
driver.get('https://www.instagram.com/sergio.alonso.almeida/')

# ---------------------------------LIKES-------------------------------------------
i = 0
for y in range(50):
    driver.implicitly_wait(1000)
    driver.find_element_by_class_name('_9AhH0').click()
    element_image = driver.find_elements_by_class_name('_9AhH0')
    print(len(element_image))

    for x in element_image:
        # -------------------- Itera dentro da imagem -------------------------
        # element_dislike = driver.find_elements_by_css_selector(
        #     "[aria-label='Descurtir']")

        # if(element_dislike):
        #     driver.find_element_by_class_name('_65Bje').click()

        element = driver.find_elements_by_css_selector(
            "[aria-label='Curtir']")
        for x in element:
            driver.implicitly_wait(530)
            print(f'like {i}')

            WebDriverWait(driver, 80).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[aria-label='Curtir']"))).click()
            i += 1
        driver.implicitly_wait(2000)

        driver.find_element_by_class_name('_65Bje').click()
        # ---------------------------------------------------------------------
