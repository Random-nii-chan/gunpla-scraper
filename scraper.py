import re
from math import ceil
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from kit import Kit

# inspired from https://stackoverflow.com/a/61433559/
def print_progress(cur,total,length=20,title="In Progress"):
    done = ceil((cur*length)/total)
    remain = length-done

    done_str = '#'*int(done)
    remain_str = '-'*int(remain)
    cur_str = '0'*int(len(str(total))-len(str(cur)))+str(cur)

    print(f'\t⌛ {title}: [{done_str}{remain_str}] {cur_str}/{total} collected.', end='\r')
    if total == cur:
        print('\t✅')

def bypass_cookies(driver) :
    # bypassing cookies prompt window
    try :
        wait = WebDriverWait(driver,1)
        cookieAcceptation = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.NN0_TB_DIsNmMHgJWgT7U.XHcr6qf5Sub2F2zBJ53S_')))
        cookieAcceptation.click()
        print("Cookies passed!")
    except TimeoutException:
        pass

def scrape(driver,id_manager,target):
    print("-----")
    print(f'Scraping kits from {target.url}...')

    driver.get(target.url)
    bypass_cookies(driver)

    all_kits = [] # used to store dictionaries
    elements = [] # used to count the kit total

    # getting all tables
    tables =  driver.find_elements(By.CSS_SELECTOR,".tabber.tabberlive")
    for table in tables :
        years = table.find_elements(By.CSS_SELECTOR, "ul.tabbernav>li>a")
        # getting years as strings
        years = list(map(lambda l : l.text, years))
        for y in years :
            # fetching all kits for this year
            try :
                # failsafe mechanism to prevent skipping of first kit in case of table header in <thead>
                table.find_element(By.TAG_NAME,f'div.tabbertab[title=\"{str(y)}\"] thead')
                kits = table.find_elements(By.CSS_SELECTOR,f'div.tabbertab[title=\"{str(y)}\"] tbody tr')
            except NoSuchElementException :
                kits = table.find_elements(By.CSS_SELECTOR,f'div.tabbertab[title=\"{str(y)}\"] tr:nth-child(n+2)')
            for k in kits:
                elements.append(k)
    total_kits=len(elements)
    parsed_kits=0
    for k in elements :
        # WebElements containing values
        attributesAsElements = k.find_elements(By.CSS_SELECTOR,"td")
        # Encoding values as strings
        attributes = list(map(lambda element : element.get_attribute('textContent').strip(), attributesAsElements))
        # print(attributes)
        # fetching image
        try :
            imageLink = attributesAsElements[0].find_element(By.CSS_SELECTOR,"a.image").get_attribute("href").strip()
        except NoSuchElementException :
            imageLink = None
        # extracting year of release
        try : 
            releaseYear = int(re.search("\\d{4}",attributes[4]).group(0))
        except :
            releaseYear = None

        # Checking if model is p-bandai
        isPbandai = "p-bandai" in attributes[5].lower()

        kit = Kit(
            id_manager.next_id(), 
            attributes[1], #model
            attributes[2], #series
            releaseYear, 
            attributes[5], #notes
            imageLink, 
            target.grade, 
            target.scale,
            isPbandai,
            target.variation
        )
        all_kits.append(kit.json())
        parsed_kits+=1
        print_progress(parsed_kits,total_kits)
        
    return driver,id_manager,all_kits