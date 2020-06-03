# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:52:57 2020

@author: tony
"""

import pickle
import os
from scraping.helper import scroll_down, get_links, get_article_text
from scraping.helper import get_driver

# specify url
SEARCH_TERM = 'xgboost'
SAVE_DIR = 'scraping/data'

url = 'https://medium.com/search?q=' + '%22' + SEARCH_TERM.replace(' ', '%20')  +'%22'

# instantiate webdriver
# driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.FIREFOX)
driver = get_driver()

# load webpage
driver.get(url)
assert "Medium" in driver.page_source

# page is loaded dynamically so we need to scroll to bottom first
# scroll_down(driver, pause_time = 1, scroll_limit = 5)
scroll_down(driver, pause_time = 2)

# get links to all articles 
links = get_links(driver)
links

# reinstantiate driver (not sure why this is needed again)
driver = get_driver()

# text = get_article_text(links, driver, pause_time = 4, article_limit = 5)
text = get_article_text(links, driver, pause_time = 4)        


# -----------------------------------------------------------------------------
# 5. save results

links_name = 'links_' + SEARCH_TERM.replace(' ', '_') +'.p'
text_name = 'text_' + SEARCH_TERM.replace(' ', '_') +'.p'

pickle.dump(links, open(os.path.join(SAVE_DIR, links_name), "wb"))
pickle.dump(text, open(os.path.join(SAVE_DIR, text_name), "wb"))




