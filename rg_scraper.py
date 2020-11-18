from re import search
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

driver.get("https://gundam.fandom.com/wiki/Real_Grade")

# bypassing cookies prompt window
wait = WebDriverWait(driver,10)
cookieAcceptation = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.NN0_TB_DIsNmMHgJWgT7U.XHcr6qf5Sub2F2zBJ53S_')))
cookieAcceptation.click()

# getting all tables
tables =  driver.find_elements(By.CSS_SELECTOR,".tabber.tabberlive")

for table in tables :
    years = table.find_elements(By.CSS_SELECTOR, "ul.tabbernav>li>a")
    # getting years as strings
    years = list(map(lambda l : l.text, years))
    for y in years : 
        # fetching all kits for this year
        kits = table.find_elements(By.CSS_SELECTOR,f'div.tabbertab[title=\"{str(y)}\"] tr:nth-child(n+2)')
        for k in kits :
            # WebElements containing values
            attributesAsElements = k.find_elements(By.CSS_SELECTOR,"td")
            # Encoding values as strings
            attributes = list(map(lambda element : element.get_attribute('textContent').strip(), attributesAsElements))
            # check if a valid kit ID exists
            try:
                attributes[0] = re.search("^[0-9a-zA-Z-\\/]+",attributes[0]).group(0)
            except :
                attributes[0] = "N/A"
            # fetching image
            try :
                imageLink = attributesAsElements[0].find_element(By.CSS_SELECTOR,"a.image").get_attribute("href").strip()
            except NoSuchElementException :
                imageLink = None
            # extracting year of release
            try : 
                attributes[4] = int(re.search("\d{4}$",attributes[4]).group(0))
            except :
                attributes[4] = 1970

            kit = Kit(attributes, imageLink, "RG", "1/144")

            print(kit.json())
            print("--------")
            
driver.quit()