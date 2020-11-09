import re
from kit import Kit
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# set selenium browser as headless firefox
headless = Options()
headless.headless = True
driver = webdriver.Firefox(options=headless)

driver.get("https://gundam.fandom.com/wiki/Real_Grade#Regulars_and_Special_Editions")

wait = WebDriverWait(driver,10)
cookieAcceptation = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.NN0_TB_DIsNmMHgJWgT7U.XHcr6qf5Sub2F2zBJ53S_')))
cookieAcceptation.click()

tables =  driver.find_elements(By.CSS_SELECTOR,".tabber.tabberlive")

for table in tables :
    years = table.find_elements(By.CSS_SELECTOR,".tabbernav>li>a")
    years = list(map(lambda y : y.text, years))
    print(years)