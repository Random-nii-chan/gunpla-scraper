from scraper import scrape
import selenium_maker as sm
from id_manager import IdManager as IDM
from series_isolator import isolate
import json
import time

def export_json(data,filename) :
    print("Exporting outputs as "+filename+"...")
    with open(filename,"w") as outfile :
        json.dump(data,outfile)
    print("Finished exporting.")


props = [
    {"grade":"Haropla","url":"https://gundam.fandom.com/wiki/Haropla"},
    {"grade":"RG","scale":"1/144","url":"https://gundam.fandom.com/wiki/Real_Grade"},
    {"grade":"MG","scale":"1/100","url":"https://gundam.fandom.com/wiki/Master_Grade"},
    {"grade":"RE/100","scale":"1/100","url":"https://gundam.fandom.com/wiki/Reborn-One_Hundred"},
    {"grade":"PG","scale":"1/60","url":"https://gundam.fandom.com/wiki/Perfect_Grade"},
    {"grade":"HG","variation":"Universal Century","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Universal_Century"},
    {"grade":"HG","variation":"Gundam 00","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Gundam_00"},
    {"grade":"HG","variation":"AGE","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Gundam_AGE"},
    {"grade":"HG","variation":"Gundam SEED","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Gundam_SEED"},
    {"grade":"HG","variation":"Build Divers Re:RISE","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Build_Divers_Re:RISE"},
    {"grade":"HG","variation":"Petit'gguy","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Petit%27gguy"},
    {"grade":"HG","variation":"Gundam The Origin","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Gundam_The_Origin"},
    {"grade":"HG","variation":"Build Fighters","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Build_Fighters"},
    {"grade":"HG","variation":"Build Divers","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Build_Divers"},
    {"grade":"HG","variation":"IRON-BLOODED ORPHANS","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_IRON-BLOODED_ORPHANS"},
    {"grade":"HG","variation":"Build Divers Re:RISE","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Build_Divers_Re:RISE"},
    {"grade":"HG","variation":"Reconguista in G","scale":"1/144","url":"https://gundam.fandom.com/wiki/High_Grade_Reconguista_in_G"},
    {"grade":"HG","variation":"Fighting Action Endless Waltz Series","scale":"1/144","url":"https://gundam.fandom.com/wiki/1/144_High_Grade_Fighting_Action_Endless_Waltz_Series"},
    {"grade":"Hi-res","scale":"1/100","url":"https://gundam.fandom.com/wiki/Hi-Resolution_Model"},
    {"grade":"SD","variation":"Cross Silhouette","url":"https://gundam.fandom.com/wiki/SD_Gundam_Cross_Silhouette"},
    {"grade":"SD","variation":"BB Senshi","url":"https://gundam.fandom.com/wiki/SD_Gundam_BB_Senshi"},
    {"grade":"SD","variation":"Ex-Standard","url":"https://gundam.fandom.com/wiki/SD_Gundam_EX-Standard"}
]

driver = sm.make_driver()
manager = IDM()
all_kits = []

for p in props :
    kits = []
    driver,manager,kits = scrape(driver,manager,p["grade"],p["scale"] if "scale" in p else None,p["url"],p["variation"] if "variation" in p else None)
    all_kits+=kits
    time.sleep(1)

driver.quit()

export_json(all_kits,"output.json")

print("webscraping done !")