from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def make_driver():
    print("creating headless firefox browser...")
    headless = Options()
    headless.headless = True
    wd = webdriver.Firefox(options=headless)
    print("Done.")
    return wd