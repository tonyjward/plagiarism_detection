# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:12:47 2020

@author: tony
"""

import time
from bs4 import BeautifulSoup

def scroll_down(driver, pause_time = None, scroll_limit = None):
    '''
    Scrolls down to the end of the search results
    Code based on:
    https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
    
    Arguments:
        driver      : an object of class webdriver from the Selenium package
        pause_time  : float - number of seconds to wait between scrolls
        scroll_limit: int - limit the number of scrolls (useful for testing)
        
    '''
    if pause_time is None:
        raise ValueError('You must specify a pause_time')
        
    time.sleep(pause_time) # start with a pause 
            
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    i = 0

    while True:
        print('page: ', i)
        
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        # Wait to load page
        time.sleep(pause_time)
    
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print('We scrolled to the bottom')
            break
        last_height = new_height
        
        i += 1
        
        if i == scroll_limit:
            print(f'We reached the scroll limit of {scroll_limit}')
            break
        
def get_links(driver, html_class = "button button--smaller button--chromeless u-baseColor--buttonNormal"):
    '''
    Scrolls down to the end of the search results
    Code based on:
    https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
    
    Arguments:
        driver      : an object of class webdriver from the Selenium package
        pause_time  : float - number of seconds to wait between scrolls
        scroll_limit: int - limit the number of scrolls (useful for testing)
        
    Return:
            list of strings with each element a html link
        
    '''
    outer_html = driver.execute_script("return document.documentElement.outerHTML")

    soup = BeautifulSoup(outer_html, 'html.parser')
     
    links=[]
    for result in soup.find_all(class_= html_class):
            links.append(result.get('href'))
            
    unique_links = set(links)
    
    print(f'{len(links)} links found')
    print(f'{len(unique_links)} of those were unique')
    
    return unique_links
    
    
    