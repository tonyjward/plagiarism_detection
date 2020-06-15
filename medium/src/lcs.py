import pickle
import os
from sys import argv
import numpy as np
import itertools
import pandas as pd
import time
import multiprocessing
from tqdm import tqdm

from src.utils.create_features import lcs_norm_word, lcs_wrapper

script, search_terms, save_dir = argv
search_list = list(map(str, search_terms.strip('[]').split(',')))

def main(search_list):
    for search_term in search_list:
        try:
            print(f"Calculating longest common subsequence for {search_term}")

            # load data
            filename = search_term.replace(' ', '_') +'_data_dict.p'  
            data_dict = pickle.load(open(os.path.join(save_dir, filename), "rb"))
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
            filename = search_term.replace(' ', '_') +'_lcs.p'   
            pickle.dump(pairwise_lcs, open(os.path.join(save_dir, filename), "wb"))

            print(f"Calculate longest common subsequence for {search_term}")
        except Exception:
            print(f"We failed to calculate longest common subsequence for {search_term}")
            pass

if __name__ =='__main__':
    main(search_list)





  
    
