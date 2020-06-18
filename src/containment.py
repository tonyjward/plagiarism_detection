import pickle
import os
import sys
from sys import argv
import traceback
import numpy as np
import itertools
import pandas as pd
import time
import multiprocessing
from tqdm import tqdm

from src.utils.create_features import ngram_array, containment, calculate_containment, containment_wrapper

script, search_terms, save_dir = argv
search_list = list(map(str, search_terms.strip('[]').split(',')))

def main(search_list):
    '''
    Calculates the containment for a list of article pairs.

    Arguments:
        search_list (list): a list of search terms that have been manipulated using manipulate_data.py e.g. ['random forest', 'linear regression']

    Returns:
        Nothing is returned however for each search_term in search_list the following file is stored in the save_dir directory
            <search_term>_containment.p - a pickled list containing the containment for article pairs stored in <search_term>_article_pairs.p
    '''
    for search_term in search_list:
        try:  
            print(f"Calculating containmnet for {search_term}")
            
            # load data
            filename = search_term.replace(' ', '_') +'_data_dict.p'  
            data_dict = pickle.load(open(os.path.join(save_dir, filename), "rb"))
            article_pairs = data_dict['article_pairs']

            # create as many processes as there are CPUs on your machine
            num_processes = multiprocessing.cpu_count()
            
            # calculate containment
            print('calculating containment in parallel')
            with multiprocessing.Pool(num_processes) as pool:
                pairwise_containment = list(tqdm(pool.imap(containment_wrapper, article_pairs), total = len(article_pairs)))
                pool.close()
                pool.join()

            # save data
            filename = search_term.replace(' ', '_') +'_containment.p'   
            pickle.dump(pairwise_containment, open(os.path.join(save_dir, filename), "wb"))

            print(f"Containment calculated for {search_term}")
        except Exception:
            print(f"We failed to calculate containmnet for {search_term}.")
            traceback.print_exc()
            pass

if __name__ =='__main__':
    main(search_list)

    



  
    
