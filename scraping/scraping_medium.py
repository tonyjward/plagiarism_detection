# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:52:57 2020

@author: tony
"""

import pickle

from scraping.helper import scroll_down, get_links, get_article_text
from scraping.helper import get_driver

# specify url
URL = 'https://medium.com/search?q=xgboost' # 'https://medium.com/search?q=%22drawing%20pin%22'

# instantiate webdriver
# driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.FIREFOX)
driver = get_driver()

# load webpage
driver.get(URL)
assert "Medium" in driver.page_source

# page is loaded dynamically so we need to scroll to bottom first
scroll_down(driver, pause_time = 1, scroll_limit = 5)
# scroll_down(driver, pause_time = 2)

# get links to all articles 
links = get_links(driver)
links

# reinstantiate driver (not sure why this is needed again)
driver = get_driver()

text = get_article_text(links, driver, pause_time = 4, article_limit = 5)
# text = get_article_text(links, driver, pause_time = 4)        


#driver.get(links[0])
#outer_html = driver.execute_script("return document.documentElement.outerHTML")
#soup = BeautifulSoup(outer_html, 'html.parser')
#text.append(soup.get_text())

# -----------------------------------------------------------------------------
# 5. save results

pickle.dump(links, open("scraping/data/links3.p", "wb"))
pickle.dump(text, open("scraping/data/text3.p", "wb"))

links2 = pickle.load(open("scraping/data/links.p", "rb"))
text2 = pickle.load(open("scraping/data/text.p", "rb"))
