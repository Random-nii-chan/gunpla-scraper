import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from id_manager import IdManager as IDM
from scraper import scrape
from scraper import bypass_cookies
from target import Target

def export_json(data,filename) :
    print("Exporting outputs as "+filename+"...")
    with open(filename,"w") as outfile :
        json.dump(data,outfile)
    print("Finished exporting.")

def make_driver(hl):
    print("Creating headless firefox browser...")
    headless = Options()
    headless.headless = hl
    wd = webdriver.Firefox(options=headless)
    print("Done.")
    return wd

# commented fetch_targets are waiting for wiki modification
# self,grade,url,scale=None,variation=None
targets = [
    Target("Haropla","https://gundam.fandom.com/wiki/Haropla"),
    Target("RG","https://gundam.fandom.com/wiki/Real_Grade","1/144"),
    Target("MG","https://gundam.fandom.com/wiki/Master_Grade","1/100"),
    Target("RE/100","https://gundam.fandom.com/wiki/Reborn-One_Hundred","1/100"),
    Target("PG","https://gundam.fandom.com/wiki/Perfect_Grade","1/60"),
    Target("HG","https://gundam.fandom.com/wiki/High_Grade_Universal_Century","1/144","Universal Century"),
    Target("HG","https://gundam.fandom.com/wiki/High_Grade_Gundam_00","1/144","Gundam 00"),
    Target("HG","https://gundam.fandom.com/wiki/High_Grade_Gundam_AGE","1/144","AGE"),
    Target("HG","https://gundam.fandom.com/wiki/High_Grade_Gundam_SEED","1/144","Gundam SEED"),
    Target("HG","https://gundam.fandom.com/wiki/High_Grade_Build_Divers_Re:RISE","1/144"," Build Divers Re:RISE"),
    Target("HG","https://gundam.fandom.com/wiki/High_Grade_Petit%27gguy",variation="Petit'gguy"),
    Target("HG","https://gundam.fandom.com/wiki/High_Grade_Gundam_The_Origin","1/144","Gundam The Origin"),
    Target("HG","https://gundam.fandom.com/wiki/High_Grade_Build_Divers","1/144","Build Divers"),
    Target("HG","https://gundam.fandom.com/wiki/High_Grade_IRON-BLOODED_ORPHANS","1/144","IRON-BLOODED ORPHANS"),
    Target("HG","https://gundam.fandom.com/wiki/High_Grade_Reconguista_in_G","1/144","Reconguista In G"),
    Target("HG","https://gundam.fandom.com/wiki/1/144_High_Grade_Fighting_Action_Endless_Waltz_Series","1/144","Fighting Action Endless Waltz Series"),
    Target("Hi-res","https://gundam.fandom.com/wiki/Hi-Resolution_Model","1/100"),
    Target("SD","https://gundam.fandom.com/wiki/SD_Gundam_Cross_Silhouette",variation="Cross Silouhette"),
    Target("SD","https://gundam.fandom.com/wiki/SD_Gundam_BB_Senshi",variation="BB Senshi"),
    Target("SD","https://gundam.fandom.com/wiki/SD_Gundam_EX-Standard",variation="Ex-Standard")
]

driver = make_driver(True)
kit_id_manager = IDM()
all_kits = []

for t in targets :
    kits = []
    driver,kit_id_manager,kits = scrape(driver,kit_id_manager,t)
    all_kits+=kits
    time.sleep(1)

driver.quit()

export_json(all_kits,"output.json")

print("webscraping done !")