from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from connection_driver import connection
from helper import DRIVER_PATH_CHROME
from selenium.webdriver.common.keys import Keys
import time


class history_bot:
    def __init__(self):
        # ----------- descomentar se chamar o script followers ------
        self.driver = webdriver.Chrome(
            executable_path=DRIVER_PATH_CHROME)
        connection(self.driver)

    def hist_access(self):
        try:
            self.driver.find_element_by_class_name('Fd_fQ').click()
        except NoSuchElementException:
            self.driver.find_element_by_class_name('FhutL').click()

        except IndexError:
            pass

    def reaction(self, position):
        # Action
        try:
            self.driver.find_element_by_class_name('Xuckn').click()
            self.driver.find_elements_by_class_name('IbKC8')[
                position].click()
            time.sleep(2)
            self.driver.find_element_by_class_name('FhutL').click()
        except NoSuchElementException:
            self.driver.find_element_by_class_name('FhutL').click()

        except IndexError:
            pass


bot = history_bot()
bot.hist_access()

for i in range(400):
    # if(i % 2 == 0):
    #     print(i, 'jump')
    #     bot.hist_access()
    if i <= 150:
        for i in range(3):
            print(i, 'jump')
            bot.hist_access()
        print(i, 'nota 100')
        bot.reaction(7)
    else:
        for i in range(3):
            print(i, 'jump')
            bot.hist_access()
        print(i, 'nota 100')
        print(i, 'palminha')
        bot.reaction(4)
