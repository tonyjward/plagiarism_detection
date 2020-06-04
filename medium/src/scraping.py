# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:12:47 2020

@author: tony
"""

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_driver(command_executor = "http://127.0.0.1:4444/wd/hub",
                       desired_capabilities = DesiredCapabilities.FIREFOX):
    'Instantiate a Selenium Webdriver'
    
    return webdriver.Remote(command_executor, desired_capabilities)


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
    Gets all html links relating to a specific html_class for an instantiated webdriver
    
    Arguments:
        driver      : (webdriver) an object of class webdriver from the Selenium package
        html_class  : (str) the class of html links to return
        
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
    
    return list(unique_links)

def get_article_text(links, driver, pause_time = None, article_limit = None):
    '''
    Gets article text from a series of html links
    
    Arguments:
        links       : an list of html links
        driver      : an object of class webdriver from the Selenium package
        pause_time  : float - number of seconds to wait between articles
        
    Returns:
        a dictionary containing the following
            links_worked: (list) of html links we could retrieve text for
            articles:     (list) of article texts
            links_failed  (list) of html links we could not retrieve text
    '''        
        
    if len(links) == 0:
        raise ValueError('You provided an empty list')
    
    links_worked = []
    articles = []
    links_failed = []

    i = 0

    for link in links:
        print(f'Article {i} of {len(links)}')
        print(link)
        
        try:
            driver.get(link)
            outer_html = driver.execute_script("return document.documentElement.outerHTML")
            soup = BeautifulSoup(outer_html, 'html.parser')
            articles.append(soup.get_text())
            links_worked.append(link)
        except:           
            print(f"We got an error for link at position {i}")
            print(sys.exc_info()[0])
            links_failed.append(link)
        finally:
            if i == article_limit:
                print(f'We reached the article limit of {article_limit}')
                return {'links_worked': links_worked, 'articles': articles, 'links_failed': links_failed}
            i += 1
        
    return {'links_worked': links_worked, 'articles': articles, 'links_failed': links_failed}
    


    
    
    