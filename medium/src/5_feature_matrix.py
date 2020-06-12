import pickle
import os
import numpy as np
import pandas as pd


SEARCH_TERM = 'xgboost'
SAVE_DIR = '../data'

def main():
    print('Creating feature matrix')
    
    # load data frame
    filename = SEARCH_TERM.replace(' ', '_') +'_data_dict.p'  
    data_dict = pickle.load(open(os.path.join(SAVE_DIR, filename), "rb"))
    df = data_dict['df']

    # load containment
    filename = SEARCH_TERM.replace(' ', '_') +'_containment.p'  
    pairwise_containment = pickle.load(open(os.path.join(SAVE_DIR, filename), "rb"))

    # load containment
    filename = SEARCH_TERM.replace(' ', '_') +'_lcs.p'  
    pairwise_lcs = pickle.load(open(os.path.join(SAVE_DIR, filename), "rb"))

    # join data
    assert df.shape[0] == len(pairwise_containment) == len(pairwise_lcs)
    df['c_20'] = pairwise_containment
    df['lcs_word'] = pairwise_lcs

    # remove comparisons between the same author
    df = df.loc[df['author_A'] != df['author_B']].reset_index(drop=True)

    # save data
    filename = SEARCH_TERM.replace(' ', '_') +'_feature_matrix.p'   
    pickle.dump(df, open(os.path.join(SAVE_DIR, filename), "wb"))

    print('Created feature matrix')

if __name__ =='__main__':
    main()

    
