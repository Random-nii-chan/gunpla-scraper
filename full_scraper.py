import json
import time
from selenium_maker import SeleniumMaker
from id_manager import IdManager
from scraper import scrape
from scraper import bypass_cookies
from series_isolator import isolate

def export_json(data,filename) :
    print("Exporting outputs as "+filename+"...")
    with open(filename,"w") as outfile :
        json.dump(data,outfile)
    print("Finished exporting.")

def target(grade,url,scale=None,variation=None):
    root = {
        "grade": grade,
        "url": url
    }
    if scale != None:
        root["scale"] = scale
    if variation != None:
        root["variation"] = variation
    return root

# commented fetch_targets are waiting for wiki modification
targets = [
    # create_fetch_target(grade="SD",variation="Ex-Standard",url="https://gundam.fandom.com/wiki/SD_Gundam_EX-Standard"),
    target(grade="Haropla",url="https://gundam.fandom.com/wiki/Haropla"),
    target(grade="RG",scale="1/144",url="https://gundam.fandom.com/wiki/Real_Grade"),
    target(grade="MG",scale="1/100",url="https://gundam.fandom.com/wiki/Master_Grade"),
    target(grade="RE/100",scale="1/100",url="https://gundam.fandom.com/wiki/Reborn-One_Hundred"),
    target(grade="PG",scale="1/60",url="https://gundam.fandom.com/wiki/Perfect_Grade"),
    target(grade="HG",variation="Universal Century",scale="1/144",url="https://gundam.fandom.com/wiki/High_Grade_Universal_Century"),
    target(grade="HG",variation="Gundam 00",scale="1/144",url="https://gundam.fandom.com/wiki/High_Grade_Gundam_00"),
    target(grade="HG",variation="AGE",scale="1/144",url="https://gundam.fandom.com/wiki/High_Grade_Gundam_AGE"),
    target(grade="HG",variation="Gundam SEED",scale="1/144",url="https://gundam.fandom.com/wiki/High_Grade_Gundam_SEED"),
    target(grade="HG",variation="Build Divers Re:RISE",scale="1/144",url="https://gundam.fandom.com/wiki/High_Grade_Build_Divers_Re:RISE"),
    target(grade="HG",variation="Petit'gguy",scale="1/144",url="https://gundam.fandom.com/wiki/High_Grade_Petit%27gguy"),
    target(grade="HG",variation="Gundam The Origin",scale="1/144",url="https://gundam.fandom.com/wiki/High_Grade_Gundam_The_Origin"),
    target(grade="HG",variation="Build Divers",scale="1/144",url="https://gundam.fandom.com/wiki/High_Grade_Build_Divers"),
    target(grade="HG",variation="IRION-BLOODED ORPHANS",scale="1/144",url="https://gundam.fandom.com/wiki/High_Grade_IRON-BLOODED_ORPHANS"),
    target(grade="HG",variation="Reconguista in G",scale="1/144",url="https://gundam.fandom.com/wiki/High_Grade_Reconguista_in_G"),
    target(grade="HG",variation="Fighting Action Endless Waltz Series",scale="1/144",url="https://gundam.fandom.com/wiki/1/144_High_Grade_Fighting_Action_Endless_Waltz_Series"),
    target(grade="Hi-res",scale="1/100",url="https://gundam.fandom.com/wiki/Hi-Resolution_Model"),
    target(grade="SD",variation="Cross Silouhette",url="https://gundam.fandom.com/wiki/SD_Gundam_Cross_Silhouette"),
    target(grade="SD",variation="BB Senshi",url="https://gundam.fandom.com/wiki/SD_Gundam_BB_Senshi")
]

sm = SeleniumMaker()
driver = sm.make_driver()

kit_id_manager = IdManager.get_instance()

all_kits = []

for t in targets :
    kits = []
    driver,kit_id_manager,kits = scrape(
        driver,
        kit_id_manager,
        t["grade"],
        t["scale"] if "scale" in t else None,
        t["url"],
        t["variation"] if "variation" in t else None
    )
    all_kits+=kits
    time.sleep(1)

driver.quit()

export_json(all_kits,"output.json")

print("webscraping done !")