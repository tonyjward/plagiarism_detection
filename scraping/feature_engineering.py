# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 09:29:11 2020

@author: tony
"""
import pickle

# specify url
SEARCH_TERM = 'xgboost'
SAVE_DIR = 'scraping/data'

# -----------------------------------------------------------------------------
# 5. save results

links = pickle.load(open(os.path.join(SAVE_DIR, links_name), "rb"))
text = pickle.load(open(os.path.join(SAVE_DIR, text_name), "rb"))

# How long are the articles
len(text[1].split())

import re

def remove_junk(article, remove_after = 'Written by'):
    '''
    Removes unncessary text found at bottom of article such as links
    to other articles
    
    Arguments:
        article: (str) raw article text
    
    Returns:
        (article_cleaned, article_junk) splits out article text vs junk text
    '''
    
    junk_position = re.search(remove_after, article)
    
    article_cleaned = article[:junk_position.start()]
    article_junk = article[junk_position.start():]
    
    return (article_cleaned, article_junk)

def clean_articles(articles_raw):
    '''
    Removes junk text from a list of articles
    
    Arguments:
        articles_raw: list of raw article text
        
    Returns:
        articles_clean: 
    '''

    return [remove_junk(article) for article in articles_raw]
        
articles_clean = clean_articles(text)

for i in range(len(text)):
    print(i)
    clean, junk = remove_junk(text[i])



