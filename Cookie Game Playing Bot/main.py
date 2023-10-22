from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

import time

URL = 'https://orteil.dashnet.org/experiments/cookie/'

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Edge(options=options)
driver.get(url=URL)

cookie_button = driver.find_element(By.ID, 'cookie')
prices = []
buttons = []
money = 0


def print_result():
    cps_element = driver.find_element(By.ID, 'cps')
    print(cps_element.text)


def update_money():
    global money
    money_str = driver.find_element(By.ID, 'money')
    money = int(money_str.text.replace(',',''))


def get_buttons():
    global buttons
    buttons.clear()
    upgrade_elements = driver.find_elements(By.CSS_SELECTOR, 'div[id="store"] div[id^="buy"]')
    for element in upgrade_elements:
        buttons.append(element)


def update_prices():
    prices.clear()
    upgrade_elements = driver.find_elements(By.CSS_SELECTOR, 'div[id="store"] div[id^="buy"]')
    for element in upgrade_elements:
        try:
            price_str = element.text.split('\n')[0].split('-')[1].strip()
            price_int = int(price_str.replace(',', ''))
            prices.append(price_int)
        except IndexError:
            pass


def get_affordable_upgrade():
    for index in range(len(prices)-1, -1, -1):
        if prices[index] <= money:
            return prices.index(prices[index])
    return None


def upgrade():
    index = get_affordable_upgrade()
    if index is not None:
        try:
            get_buttons()
            buttons[index].click()
        except IndexError:
            pass


def click_on_cookie():
    cookie_button.click()


time_temp = int(time.time())
start_time = time_temp
ending_time = start_time + 60 * 5
last_upgraded_time = None

while ending_time >= int(time.time()):
    click_on_cookie()

    if time_temp % 5 == 0 and last_upgraded_time != time_temp:
        print('is upgrading and remaining time is ' + str(ending_time - time_temp))
        last_upgraded_time = time_temp
        is_upgrading = True
        update_money()
        update_prices()
        upgrade()

    time_temp = int(time.time())

print_result()




