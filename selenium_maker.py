from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def make_driver():
    headless = Options()
    headless.headless = True
    return webdriver.Firefox(options=headless)