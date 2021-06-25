import helper
from main import instaBot
from arduino import ArduinoLeds

lights = ArduinoLeds()
bot = instaBot(helper.LOGIN, helper.PASSWORD, helper.DRIVER_PATH_CHROME)

lights.yellow_led_on()
bot.signIn()

lights.blue_led_blink()
