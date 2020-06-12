import pickle
import os

from utils.cleaning import remove_junk, clean_articles

SEARCH_TERM = 'nasty surprise'
SAVE_DIR = '../data'

def main():
    # load data
    filename_links = SEARCH_TERM.replace(' ', '_') +'_links.p'
    filename_articles = SEARCH_TERM.replace(' ', '_') +'_articles.p' 
    links = pickle.load(open(os.path.join(SAVE_DIR, filename_links), "rb"))  
    articles = pickle.load(open(os.path.join(SAVE_DIR, filename_articles), "rb"))

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
    filename = SEARCH_TERM.replace(' ', '_') +'_articles_clean.p'   
    pickle.dump(articles_clean, open(os.path.join(SAVE_DIR, filename), "wb"))

    print('Data has been seperated into author, article and junk')
    if author_list.count('Blank') > 0:
        print(f"There are {author_list.count('Blank')} articles with  data issues - these are identifed as 'Blank'")

if __name__ =='__main__':
    main()

    

        

