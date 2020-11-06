import re
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# set selenium browser as headless firefox
headless = Options()
headless.headless = True
driver = webdriver.Firefox(options=headless)

details = ["Number","Model","Series","Yen Price","Release Date","Notes"]

driver.get("https://gundam.fandom.com/wiki/Real_Grade#Regulars_and_Special_Editions")

table =  driver.find_element(By.CSS_SELECTOR,".tabber.tabberlive")
years = table.find_elements(By.CSS_SELECTOR, "ul.tabbernav>li>a")
years = map(lambda l : l.text, years)

for y in years : 
    kits = table.find_elements(By.CSS_SELECTOR,f'div.tabbertab[title=\"{str(y)}\"] tr:nth-child(n+2)')
    for k in kits : 
        for d in details : 
            index = details.index(d)
            element = k.find_element(By.CSS_SELECTOR,"td:nth-child("+str(index+1)+")")
            info = element.get_attribute('textContent').strip()
            if index == 0 :
                try : 
                    info = re.search("^[0-9a-zA-Z-\/]+",info).group(0)
                except : 
                    info = "N/A"
                # fetching image
                try :
                    imageLink = element.find_element(By.CSS_SELECTOR,"a.image").get_attribute("href").strip()
                    print(f'Image Link: {imageLink}')
                except NoSuchElementException :
                    print("No Image provided")

            print(d+" : "+info)

        print("-------")

driver.quit()