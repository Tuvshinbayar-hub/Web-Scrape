from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

URL = 'https://en.wikipedia.org/wiki/Main_Page'
URL_LAB = 'http://secure-retreat-92358.herokuapp.com/'

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Edge(options=options)
driver.get(url=URL_LAB)

input_name = driver.find_element(By.NAME, 'fName')
input_name.send_keys('Tuvshuu')

input_last_name = driver.find_element(By.NAME, 'lName')
input_last_name.send_keys('G.')

email = driver.find_element(By.NAME, 'email')
email.send_keys('tuvshuu@tuvshuu.mn')

button_signup = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button_signup.click()

# statistic_element = driver.find_element(By.CSS_SELECTOR, 'a[title="Special:Statistics"]')
# search_button_element = driver.find_element(By.CSS_SELECTOR, 'a[href="/wiki/Special:Search"]')
# search_button_element.click()
#
# search_input_element = driver.find_element(By.NAME, 'search')
# search_input_element.send_keys('Python')
# search_input_element.send_keys(Keys.ENTER)
