from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = 'https://www.python.org/'

options = webdriver.EdgeOptions()
options.add_argument('--headless')
driver = webdriver.Edge(options=options)

driver.get(url=URL)

upcoming_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li')
upcoming_events_dic = {}

for i in range(len(upcoming_events)):
    upcoming_events_dic[i] = {
        'time': upcoming_events[i].text.split('\n')[0],
        'name': upcoming_events[i].text.split('\n')[1]
    }
 
print(upcoming_events_dic)

driver.quit()

