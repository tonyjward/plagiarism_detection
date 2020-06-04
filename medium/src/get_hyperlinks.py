# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:52:57 2020

@author: tony
"""

import pickle
import os
from helper import scroll_down, get_links, get_article_text
from helper import get_driver

# specify url
SEARCH_TERM = 'xgboost'
SAVE_DIR = 'data'

if __name__ == '__main__':

    url = 'https://medium.com/search?q=' + '%22' + SEARCH_TERM.replace(' ', '%20')  +'%22'

    # instantiate webdriver
    # driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.FIREFOX)
    driver = get_driver()

    # load webpage
    driver.get(url)
    assert "Medium" in driver.page_source

    # page is loaded dynamically so we need to scroll to bottom first
    # scroll_down(driver, pause_time = 1, scroll_limit = 5)
    scroll_down(driver, pause_time = 3)

    # get links to all articles 
    links = get_links(driver)
    links

    # save results
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    links_name = 'links_' + SEARCH_TERM.replace(' ', '_') +'.p'
    pickle.dump(links, open(os.path.join(SAVE_DIR, links_name), "wb"))

    print(f"We saved the file {links_name} in the {SAVE_DIR} directory")





