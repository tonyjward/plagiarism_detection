import pickle
import os
import traceback
import sys
from sys import argv
import numpy as np
import pandas as pd


script, search_terms, save_dir = argv
search_list = list(map(str, search_terms.strip('[]').split(',')))

def word_count(article):
    return len(article.split())

def main(search_list):
    '''
    Adds the containment and longest common subsequence created in containment.py and lcs.py onto the 
    dataframe created in manipulate_data.py

    Arguments:
        search_list (list): a list of search terms that have been manipulated using manipulate_data.py e.g. ['random forest', 'linear regression']

    Returns:
        Nothing is returned however for each search_term in search_list the following file is stored in the save_dir directory
            <search_term>_feature_matrix.p - a pickled dataframe containing the data frame calculated in manipulate_data.py and the two similarity features
    '''
    for search_term in search_list:
        try:
            print(f'Creating feature matrix for {search_term}')
            
            # load data frame
            filename = search_term.replace(' ', '_') +'_data_dict.p'  
            data_dict = pickle.load(open(os.path.join(save_dir, filename), "rb"))
            df = data_dict['df']

            # load containment
            filename = search_term.replace(' ', '_') +'_containment.p'  
            pairwise_containment = pickle.load(open(os.path.join(save_dir, filename), "rb"))

            # load containment
            filename = search_term.replace(' ', '_') +'_lcs.p'  
            pairwise_lcs = pickle.load(open(os.path.join(save_dir, filename), "rb"))

            # join data
            assert df.shape[0] == len(pairwise_containment) == len(pairwise_lcs)
            df['c_20'] = pairwise_containment
            df['lcs_word'] = pairwise_lcs

            # remove comparisons between the same author
            df = df.loc[df['author_A'] != df['author_B']].reset_index(drop=True)

            # calculate work count 
            print('Calculating word count for article_A')
            df['word_count_A'] = df['article_A'].map(word_count)
            print('Calculating word count for article_B')
            df['word_count_B'] = df['article_B'].map(word_count)

            # save data
            filename = search_term.replace(' ', '_') +'_feature_matrix.p'   
            pickle.dump(df, open(os.path.join(save_dir, filename), "wb"))

            print(f'Created feature matrix for {search_term}')
        except Exception:
            print(f"We failed to create the feature matrix for {search_term}")
            traceback.print_exc()
            pass

if __name__ =='__main__':
    main(search_list)

    
