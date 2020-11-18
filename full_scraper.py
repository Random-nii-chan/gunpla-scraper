from scraper import scrape
import selenium_maker as sm
import json
import time
from id_manager import IdManager as IDM

def export_json(data,filename) :
    print("Exporting outputs as "+filename+"...")
    with open(filename,"w") as outfile :
        json.dump(data,outfile)
    print("Finished exporting.")


props = [
    {"grade":"RG","scale":"1/144","url":"https://gundam.fandom.com/wiki/Real_Grade"},
    {"grade":"HG","variation":"Universal Century","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Universal_Century"},
    {"grade":"HG","variation":"Gundam 00","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Gundam_00"},
    {"grade":"HG","variation":"AGE","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Gundam_AGE"}
]

driver = sm.make_driver()
manager = IDM()
all_kits = []

for p in props :
    kits = []
    driver,manager,kits = scrape(driver,manager,p["grade"],p["scale"],p["url"],p["variation"] if "variation" in p else None)
    all_kits+=kits
    time.sleep(1)

export_json(all_kits,"output.json")

driver.quit()

print("webscraping done !")