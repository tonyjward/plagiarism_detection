# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:52:57 2020

@author: tony
"""

import pickle
import os
import time
from sys import argv

from src.utils.scraping import scroll_down, get_links, get_article_text, get_driver, login

script, search_terms, save_dir = argv
search_list = list(map(str, search_terms.strip('[]').split(',')))

def main(search_list, pause_time = 3):
    # instantiate webdriver and log in to medium
    driver = get_driver()
    login(driver)

    for search_term in search_list:
    
        # search for articles
        try:
            url = 'https://medium.com/search?q=' + '%22' + search_term.replace(' ', '%20')  +'%22'
            driver.get(url)
            assert "Medium" in driver.page_source

            # scroll down to bottom of page
            scroll_down(driver, pause_time = pause_time) # scroll_limit option available
            
            # get links to all articles 
            links = get_links(driver)

            # save links
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            filename_links = search_term.replace(' ', '_') +'_links.p'
            pickle.dump(links, open(os.path.join(save_dir, filename_links), "wb"))

            time.sleep(5)

            # get article text
            articles = get_article_text(links, driver, pause_time = pause_time)  # article_limit option available   
            
            # save results
            filename = search_term.replace(' ', '_') +'_articles.p'   
            pickle.dump(articles, open(os.path.join(save_dir, filename), "wb"))

            # Inform user of success
            print(f'Scraping for {search_term} was successful')
            print(f"We scraped {len(articles['links_worked'])} articles and had {len(articles['links_failed'])} failures")
        except Exception:
            print (f"We failed to scrape data for {search_term}")
            pass

    # close webdriver
    driver.close()

if __name__ == '__main__':
    main(search_list)

    




