import pickle
import os
import numpy as np
import itertools
import pandas as pd
import time
import multiprocessing
from tqdm import tqdm

from src.utils.create_features import lcs_norm_word, lcs_wrapper

SEARCH_TERM = 'nasty surprise'
SAVE_DIR = '../data'

def main():
    # load data
    filename = SEARCH_TERM.replace(' ', '_') +'_data_dict.p'  
    data_dict = pickle.load(open(os.path.join(SAVE_DIR, filename), "rb"))
    article_pairs = data_dict['article_pairs']

    # create as many processes as there are CPUs on your machine
    num_processes = multiprocessing.cpu_count()
    
    # calculate containment
    print('calculating containment in parallel')
    with multiprocessing.Pool(num_processes) as pool:
        pairwise_lcs = list(tqdm(pool.imap(lcs_wrapper, article_pairs), total = len(article_pairs)))
        pool.close()
        pool.join()

    # save data
    filename = SEARCH_TERM.replace(' ', '_') +'_lcs.p'   
    pickle.dump(pairwise_lcs, open(os.path.join(SAVE_DIR, filename), "wb"))

if __name__ =='__main__':
    main()





  
    
