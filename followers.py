from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from connection_driver import connection
from helper import DRIVER_PATH_CHROME
import time
import sys


class followers:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=DRIVER_PATH_CHROME)
        connection(self.driver)

    def getFollowers(self, username):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{username}")
        time.sleep(1)

        followersLink = self.driver.find_element_by_css_selector("ul li a")
        followersLink.click()

        followersList = self.driver.find_element_by_css_selector(
            "div[role='dialog'] ul"
        )

        listaLi = []
        actionChain = webdriver.ActionChains(self.driver)
        for i in range(3):
            followersList.click()
            time.sleep(0.5)
            for user in followersList.find_elements_by_css_selector("li"):
                userLink = user.find_element_by_css_selector("a").get_attribute(
                    "href"
                )

                listaLi.append(userLink)

            lista_usuarios = [link.replace(
                'https://www.instagram.com/', '')[:-1] for link in listaLi]
            print(lista_usuarios)
            print(len(lista_usuarios))

            for i in range(20):
                time.sleep(0.2)
                actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

        print(len(lista_usuarios))
        self.newList = set(lista_usuarios)

    def saveFollowers(self):
        sortedList = sorted(self.newList)

        print('Gravando....!')

        arquivo = open('users.txt', 'a')

        for user in sortedList:
            arquivo.write(f'{user}\n')

        print(f'gravados {len(sortedList)} com sucesso!')


bot = followers()
bot.getFollowers("programemos")
bot.saveFollowers()
