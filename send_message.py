from selenium import webdriver
from connection import connection
from helper import DRIVER_PATH_CHROME, cor_terminal
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# -------------------------------------LOGIN-------------------------------
# driver = webdriver.Chrome(
#     executable_path=DRIVER_PATH_CHROME)
# connection(driver)

# # --------------------------------look user--------------------------------
# user = 'saraabenedicto'
# f = open(f"data/sendmsgs/{user}.txt", "a")
# driver.get(f'https://www.instagram.com/{user}/')
# ----------------------------------------------------------------------


def send_msg(user, driver):
    welcome = (
        f'Welcome {user}!\n\n'
        f'Obrigado por seguir! Dicas de programação, video aulas\n'
        f'Interação e comunidade\n'
        f'Veja mais conteúdo no canal!\n\n'
        f'https://www.youtube.com/coisa_de_devoficial\n\n'
        f'Posso contar com a sua inscrição? :-)\n'
    )
    driver.implicitly_wait(2)
    driver.find_element_by_class_name(
        '_862NM ').click()  # - Clicka em enviar mensagem

    for x in welcome.split('\n'):
        driver.find_element_by_tag_name('textarea').send_keys(x)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(
            Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

    driver.find_element_by_tag_name('textarea').send_keys(Keys.ENTER)
