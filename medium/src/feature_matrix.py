import pickle
import os
import traceback
import sys
from sys import argv
import numpy as np
import pandas as pd


script, search_terms, save_dir = argv
search_list = list(map(str, search_terms.strip('[]').split(',')))

def main(search_list):
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

    
