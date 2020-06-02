# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:52:57 2020

@author: tony
"""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

from scraping.helper import scroll_down, get_links

# specify url
URL = 'https://medium.com/search?q=xgboost' # 'https://medium.com/search?q=%22drawing%20pin%22'

# instantiate webdriver
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.FIREFOX)

# load webpage
driver.get(URL)
assert "Medium" in driver.page_source

# page is loaded dynamically so we need to scroll to bottom first
scroll_down(driver, pause_time = 2, scroll_limit = 5)

# get links to all articles 
links = get_links(driver)
links
        





# -----------------------------------------------------------------------------
# 5. save results
import pickle
pickle.dump(links, open("links.p", "wb"))
