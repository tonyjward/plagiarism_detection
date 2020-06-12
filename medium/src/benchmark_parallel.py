import pickle
import os
import numpy as np
import itertools
import pandas as pd
import time
import multiprocessing
from tqdm import tqdm

from create_features import ngram_array, containment, calculate_containment, containment_wrapper, lcs_norm_word, lcs_wrapper

SEARCH_TERM = 'xgboost'
SAVE_DIR = '../data'

if __name__ =='__main__':

    # load data
    filename_clean_results = SEARCH_TERM.replace(' ', '_') +'_results_clean.p'  
    results = pickle.load(open(os.path.join(SAVE_DIR, filename_clean_results), "rb"))

    assert len(results['links_worked']) == len(results['articles']) == len(results['author']), 'links/articles/authors should all be same length'

    # create combinations to test
    article_indices = list(range(len(results['articles'])))
    combinations = list(itertools.combinations(article_indices,  2))
    results_df = pd.DataFrame(combinations, columns = ['A', 'B'])

    print ('Preparing results data')

    # loop over rows and populate author/link/article for results table
    n_rows = results_df.shape[0]
    author_A, author_B, link_A, link_B, article_A, article_B, article_pairs = [], [], [], [], [], [], []

    for row in range(n_rows):
        author_A.append(results['author'][results_df.loc[row, 'A']])
        author_B.append(results['author'][results_df.loc[row, 'B']])
        link_A.append(results['links_worked'][results_df.loc[row, 'A']])
        link_B.append(results['links_worked'][results_df.loc[row, 'B']])
        article_A.append(results['articles'][results_df.loc[row, 'A']])
        article_B.append(results['articles'][results_df.loc[row, 'B']])
        article_pairs.append([results['articles'][results_df.loc[row, 'A']],
                             results['articles'][results_df.loc[row, 'B']],
                             row])

    results_df['author_A'] = author_A
    results_df['author_B'] = author_B
    results_df['link_A'] = link_A
    results_df['link_B'] = link_B
    results_df['article_A'] = article_A
    results_df['article_B'] = article_B


    # subset data for testing
    results_df = results_df[:5000]
    article_pairs = article_pairs[:5000]

    # list comprehension
    print('running sequentially')
    tic = time.perf_counter()
    pairwise_containment = [containment_wrapper(x) for x in article_pairs ]
    toc = time.perf_counter()
    print(f"code ran in  {toc - tic:0.4f} seconds")

    # parallel processing
    # create as many processes as there are CPUs on your machine
    num_processes = multiprocessing.cpu_count()
    
    print('calculating containment in parallel')
    with multiprocessing.Pool(num_processes) as pool:
        pairwise_containment = list(tqdm(pool.imap(containment_wrapper, article_pairs), total = len(article_pairs)))
        pool.close()
        pool.join()

    # lcs
    # parallel processing
    # create as many processes as there are CPUs on your machine
    num_processes = multiprocessing.cpu_count()
    
    print('calculating lcs in parallel')
    with multiprocessing.Pool(num_processes) as pool:
        pairwise_lcs = list(tqdm(pool.imap(lcs_wrapper, article_pairs), total = len(article_pairs)))
        pool.close()
        pool.join()

    # list comprehension
    print('calculating lcs sequentially')
    tic = time.perf_counter()
    pairwise_lcs = [lcs_wrapper(x) for x in article_pairs ]
    toc = time.perf_counter()
    print(f"sequential pairwise_lcs code ran in  {toc - tic:0.4f} seconds")

  
    
