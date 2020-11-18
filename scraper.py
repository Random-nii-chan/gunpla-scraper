from rg_scraper import scrape as rg_scrape
import selenium_maker as sm
import json
from id_manager import IdManager as IDM

def outputting_data_as_json(data):
    print("Exporting web scraping results...")
    with open("output.json","w") as outfile :
        json.dump(all_kits,outfile)
    print("Done.")

driver = sm.make_driver()
manager = IDM()
all_kits = []

driver,manager,all_kits = rg_scrape(driver,manager)
outputting_data_as_json(all_kits)

print("webscraping done !")