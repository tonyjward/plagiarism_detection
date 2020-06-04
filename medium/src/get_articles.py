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

    # open links
    links_name = 'links_' + SEARCH_TERM.replace(' ', '_') +'.p'
    links = pickle.load(open(os.path.join(SAVE_DIR, links_name), "rb"))

    # instantiate selenium webdriver
    driver = get_driver()

    text = get_article_text(links, driver, pause_time = 4, article_limit = 5)
    # text = get_article_text(links, driver, pause_time = 4)        

    # save results
    text_name = 'text_' + SEARCH_TERM.replace(' ', '_') +'.p'
    pickle.dump(text, open(os.path.join(SAVE_DIR, text_name), "wb"))
    print(f"We saved the articles for {links_name} in the {SAVE_DIR} directory")




