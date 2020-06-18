import pickle
import os
import traceback
import sys
from sys import argv
import numpy as np
import itertools
import pandas as pd

script, search_terms, save_dir = argv
search_list = list(map(str, search_terms.strip('[]').split(',')))

def main(search_list):
    '''
    We manipulate the data so that it is in suitable format for calculating pairwise containmnet and 
    longest common subsequnce.

    Arguments:
        search_list (list): a list of search terms that have been cleaned using clean_data.py e.g ['random forest', 'linear regression']

    Returns:
        Nothing is returned however for each search_term in search_list the following file is stored in the save_dir directory
            <search_term>_data_dict.p - a pickled dictionary containing the following
                                                'df' (pandas DataFrame) - all pairwise articles including author, article text etc
                                                'article_pairs' (list)  - all pairwise articles only including article text
    '''

    for search_term in search_list:
        try:
            print (f'Manipulating data for {search_term}')

            # load data
            filename = search_term.replace(' ', '_') +'_articles_clean.p'  
            articles = pickle.load(open(os.path.join(save_dir, filename), "rb"))

            assert len(articles['links_worked']) == len(articles['articles']) == len(articles['author']), 'links/articles/authors should all be same length'

            # create combinations to test
            article_indices = list(range(len(articles['articles'])))
            combinations = list(itertools.combinations(article_indices,  2))
            df = pd.DataFrame(combinations, columns = ['A', 'B'])

            # loop over rows and populate author/link/article for results table
            n_rows = df.shape[0]
            author_A, author_B, link_A, link_B, article_A, article_B, article_pairs = [], [], [], [], [], [], []

            for row in range(n_rows):
                author_A.append(articles['author'][df.loc[row, 'A']])
                author_B.append(articles['author'][df.loc[row, 'B']])
                link_A.append(articles['links_worked'][df.loc[row, 'A']])
                link_B.append(articles['links_worked'][df.loc[row, 'B']])
                article_A.append(articles['articles'][df.loc[row, 'A']])
                article_B.append(articles['articles'][df.loc[row, 'B']])
                article_pairs.append([articles['articles'][df.loc[row, 'A']],
                                    articles['articles'][df.loc[row, 'B']],
                                    row])

            df['author_A'] = author_A
            df['author_B'] = author_B
            df['link_A'] = link_A
            df['link_B'] = link_B
            df['article_A'] = article_A
            df['article_B'] = article_B

            data_dict = {'df':df, 'article_pairs':article_pairs}

            # save data
            filename = search_term.replace(' ', '_') +'_data_dict.p'   
            pickle.dump(data_dict, open(os.path.join(save_dir, filename), "wb"))

            print (f'Dataframe created for {search_term}')
        except Exception:
            print(f"We failed to mainiuplate data for {search_term}")
            traceback.print_exc()
            pass

if __name__ =='__main__':
    main(search_list)
    



  
    
