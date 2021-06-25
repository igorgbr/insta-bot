from main import instaBot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from connection_driver import connection
from helper import DRIVER_PATH_CHROME, DRIVER_PATH_FIREFOX
import time


class Followers:
    def __init__(self, driver):
        self.driver = driver
        # ----------- descomentar se chamar o script followers ------
        # self.driver = webdriver.Chrome(
        #     executable_path=DRIVER_PATH_CHROME)
        # connection(self.driver)

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
        for i in range(20):
            try:
            # followersList.click()
                self.driver.find_element_by_class_name(
                    'isgrP').click()  # - Clicka na DIV no lugar do LI
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
                    actionChain.key_down(Keys.END).key_up(Keys.END).perform()
            except Exception:
                ...

        print(len(lista_usuarios))
        self.newList = set(lista_usuarios)

    def saveFollowers(self):
        sortedList = sorted(self.newList)

        print('Gravando....!')

        arquivo = open('new_followersB.txt', 'a')

        for user in sortedList:
            arquivo.write(f'{user}\n')

        print(f'gravados {len(sortedList)} com sucesso!')

        arquivo.close()

        arquivo = open('new_followersB.txt', 'r')
        newFollowers = sorted(set([x for x in arquivo]))

        arquivo.close()

        newListFollowersFile = open('new_followersB.txt', 'w')

        for x in newFollowers:
            newListFollowersFile.write(x)

        arquivo.close()

    def follow(self, btn_position):
        # self.driver.get(f"https://www.instagram.com/{newfollower}")
        # time.sleep(1)

        listAtt = [element.text.replace('.', '')
                   for element in self.driver.find_elements_by_class_name('g47SY ')]
        print(listAtt)
        # - Procedimento para usuarios com mais de mil seguidores
        for x in listAtt:
            if 'mil' in x:
                x = x.replace('mil', '00')
                x = x.replace(',', '')
                x = int(x)
            x = int(x)

        if(listAtt[2] >= listAtt[1]):
            print('Comparando listas de seguidores...')
            self.driver.find_elements_by_css_selector(
                'button')[btn_position].click()
            time.sleep(1)
            print('Seguindo usuario...')

    def exitAndClose(self):
        self.driver.quit()


# bot = Followers()
# bot.getFollowers("pycodebr")
# bot.saveFollowers()

# # bot.follow('karolcreates')
# bot.exitAndClose()
