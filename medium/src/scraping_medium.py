# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:52:57 2020

@author: tony
"""

import pickle
import os
from scraping import scroll_down, get_links, get_article_text, get_driver

# specify url
SEARCH_TERM = 'drawing pin'
SAVE_DIR = 'data'

if __name__ == '__main__':

    url = 'https://medium.com/search?q=' + '%22' + SEARCH_TERM.replace(' ', '%20')  +'%22'

    # instantiate webdriver
    # driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.FIREFOX)
    driver = get_driver()

    # load webpage
    driver.get(url)
    assert "Medium" in driver.page_source

    # scroll down to bottom of page
    scroll_down(driver, pause_time = 3) # scroll_limit option available
    
    # get links to all articles 
    links = get_links(driver)

    # save links
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    filename_links = SEARCH_TERM.replace(' ', '_') +'_links.p'
    pickle.dump(links, open(os.path.join(SAVE_DIR, filename_links), "wb"))

    # get article text
    results = get_article_text(links, pause_time = 4)  # article_limit option available      
      
    # save results
    filename_results = SEARCH_TERM.replace(' ', '_') +'_results.p'   
    pickle.dump(results, open(os.path.join(SAVE_DIR, filename_results), "wb"))




