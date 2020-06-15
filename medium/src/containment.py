import pickle
import os
from sys import argv
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
            print(f"We failed to calculate containmnet for {search_term}")
            pass

if __name__ =='__main__':
    main(search_list)

    



  
    
