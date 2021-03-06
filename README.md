# Gunpla scraper

Gunpla scraper is a python-written web scraper that gathers information about Gunpla (Gundam Plastic Models) from the Gundam fandom wiki.

# What is Gunpla ?

Gunpla is a portemanteau word for [Gundam Plastic Model](https://en.wikipedia.org/wiki/Gundam_model). These are plastic model kits representing bipedal war machines from the japanese media franchise [Gundam](https://en.wikipedia.org/wiki/Gundam), created in 1979 by [Yoshiyuki Tomino](https://en.wikipedia.org/wiki/Yoshiyuki_Tomino). 

Gunpla exists since 1980, and more than 2000 models have been released. In an attempt to list and organize this vast amount of kits, I decided to create an automated tool to fetch information about said model kits on the [Gundam Fandom Wiki](https://gundam.fandom.com/wiki/The_Gundam_Wiki).

# About this project

Back in 2016, [CircuitFreak](https://github.com/circuitfreak/) created a gunpla API and wrote an [article](https://medium.com/@jorick.caberio/building-a-gunpla-api-using-python-selenium-phantomjs-and-firebase-e68143d3fd3c) about the web scraper used to gather information from the Gundam Wiki.

However, 5 years later, Wikia (now Fandom) drastically changed their web page structure. Moreover, CircuitFreak's API only gathered info about Master Grades : I wanted to create a new, better written scraper that could list kits that aren't Master Grades.

Moreover, CircuitFreak's API is no longer active : I plan on using my webscraper's results to feed an API that I will create in the future. 

# How to use the web scraper

## Python version

This program uses Python 3.x to run. Make sure to install [Python's latest version](https://www.python.org/downloads/) to use the Gunpla Scraper. 

## Dependencies

Install the project's dependencies using `python -m pip install -r requirements.txt`. 

## Run!

Simply run the program using `python ./full_scraper.py` and watch the magic happen!