import pickle
import os
from sys import argv
import numpy as np
import pandas as pd


script, search_term = argv
SAVE_DIR = '../data'

def main(search_term):
    print('Creating feature matrix')
    
    # load data frame
    filename = search_term.replace(' ', '_') +'_data_dict.p'  
    data_dict = pickle.load(open(os.path.join(SAVE_DIR, filename), "rb"))
    df = data_dict['df']

    # load containment
    filename = search_term.replace(' ', '_') +'_containment.p'  
    pairwise_containment = pickle.load(open(os.path.join(SAVE_DIR, filename), "rb"))

    # load containment
    filename = search_term.replace(' ', '_') +'_lcs.p'  
    pairwise_lcs = pickle.load(open(os.path.join(SAVE_DIR, filename), "rb"))

    # join data
    assert df.shape[0] == len(pairwise_containment) == len(pairwise_lcs)
    df['c_20'] = pairwise_containment
    df['lcs_word'] = pairwise_lcs

    # remove comparisons between the same author
    df = df.loc[df['author_A'] != df['author_B']].reset_index(drop=True)

    # save data
    filename = search_term.replace(' ', '_') +'_feature_matrix.p'   
    pickle.dump(df, open(os.path.join(SAVE_DIR, filename), "wb"))

    print('Created feature matrix')

if __name__ =='__main__':
    main(search_term)

    
