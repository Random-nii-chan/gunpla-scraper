from rg_scraper import scrape as rg_scrape
import selenium_maker as sm
import json
from id_manager import IdManager as IDM

driver = sm.make_driver()
manager = IDM()
all_kits = []

driver,manager,all_kits = rg_scrape(driver,manager)

with open("rg.json","w") as outfile :
    json.dump(all_kits,outfile)

print("webscraping done !")