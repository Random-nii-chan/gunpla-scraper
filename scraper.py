import re
from kit import Kit
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# set selenium browser as headless firefox
headless = Options()
headless.headless = True
driver = webdriver.Firefox(options=headless)

# details that are fetched
details = ["Number","Model","Series","Yen Price","Release Date","Notes"]

driver.get("https://gundam.fandom.com/wiki/Real_Grade#Regulars_and_Special_Editions")
table =  driver.find_element(By.CSS_SELECTOR,".tabber.tabberlive")
years = table.find_elements(By.CSS_SELECTOR, "ul.tabbernav>li>a")
# getting years as strings
years = map(lambda l : l.text, years)

for y in years : 
    # fetching all kits for this year
    kits = table.find_elements(By.CSS_SELECTOR,f'div.tabbertab[title=\"{str(y)}\"] tr:nth-child(n+2)')
    for k in kits :
        # WebElements contenant les valeurs
        attributesAsElements = k.find_elements(By.CSS_SELECTOR,"td")

        # Valeurs encodées en tant que strings
        attributes = list(map(lambda element : element.get_attribute('textContent').strip(), attributesAsElements))
        try:
            attributes[0] = re.search("^[0-9a-zA-Z-\\/]+",attributes[0]).group(0)
        except :
            attributes[0] = "N/A"

        attributes[3] = int(re.sub("[^0-9A-Za-z]+","", attributes[3]))

        # fetching image
        try :
            imageLink = attributesAsElements[0].find_element(By.CSS_SELECTOR,"a.image").get_attribute("href").strip()
        except NoSuchElementException :
            imageLink = "No Image Provided"
        
        kit = Kit(attributes, imageLink, "RG")
        print(kit)
        print("--------")

driver.quit()