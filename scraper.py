from rg_scraper import scrape as rg_scrape
import selenium_maker as sm
from id_manager import IdManager as IDM

driver = sm.make_driver()
manager = IDM()
all_kits = []

driver,manager,all_kits = rg_scrape(driver,manager)

print(all_kits)