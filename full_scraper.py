from scraper import scrape
import selenium_maker as sm
import json
import time
from id_manager import IdManager as IDM

props = [
    {"grade":"RG","scale":"1/144","url":"https://gundam.fandom.com/wiki/Real_Grade"},
    {"grade":"HG","variation":"Universal Century","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Universal_Century"},
    {"grade":"HG","variation":"Gundam 00","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Gundam_00"}
]

driver = sm.make_driver()
manager = IDM()
all_kits = []

for p in props :
    kits = []
    driver,manager,kits = scrape(driver,manager,p["grade"],p["scale"],p["url"],p["variation"] if "variation" in p else None)
    all_kits+=kits
    time.sleep(1)

with open("output.json","w") as outfile :
    json.dump(all_kits,outfile)

driver.quit()

print("webscraping done !")