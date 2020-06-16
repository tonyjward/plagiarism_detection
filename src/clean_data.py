import pickle
import os
import traceback
import sys
from sys import argv

from src.utils.cleaning import remove_junk, clean_articles

script, search_terms, save_dir = argv
search_list = list(map(str, search_terms.strip('[]').split(',')))

def main(search_list):
    
    for search_term in search_list:
        try:
            print(f"Cleaning data for {search_term}")

            # load data
            filename_links = search_term.replace(' ', '_') +'_links.p'
            filename_articles = search_term.replace(' ', '_') +'_articles.p' 
            links = pickle.load(open(os.path.join(save_dir, filename_links), "rb"))  
            articles = pickle.load(open(os.path.join(save_dir, filename_articles), "rb"))

            # clean data
            author_list = []
            article_list = []
            junk_list = []

            for i in range(len(articles['links_worked'])):
                author, article, junk = remove_junk(articles['articles'][i])
                author_list.append(author)
                article_list.append(article)
                junk_list.append(junk)

            articles_clean = {'links_worked': articles['links_worked'], 'articles': article_list, 'author': author_list, 'junk': junk_list, 'links_failed': articles['links_failed']}

            # save data
            filename = search_term.replace(' ', '_') +'_articles_clean.p'   
            pickle.dump(articles_clean, open(os.path.join(save_dir, filename), "wb"))

            print('Data has been cleaned for {search_term}')
            if author_list.count('Blank') > 0:
                print(f"There are {author_list.count('Blank')} articles with  data issues - these are identifed as 'Blank'")
        except Exception:
            print(f"We failed to clean data for {search_term}")
            traceback.print_exc()
            pass

if __name__ =='__main__':
    main(search_list)

    

        

