from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def ngram_array(a_text, s_text, n):
    '''
    Calculate an ngram array for an answer and source text
    
    Arguments:
        a_text: answer text
        s_text: source text
        n     : choice of n-gram (1 == unigram, 2 == bigram etc)
    
    Returns:
        ngram array

    Note:   Function created as part of the plagiarism detection project 
            for udacities machine learning engineer nanodegree

    '''
    # instantiate an ngram counter
    counts = CountVectorizer(analyzer = 'word',
                             ngram_range = (n,n))
        
    # create array of n-gram counts for the answer and source text
    # here fit_transform learns the vocabulary dictionary and returns the document term matrix (in sparse format)
    ngrams = counts.fit_transform([a_text, s_text])

    return ngrams.toarray()

def containment(ngram_array):
    ''' 
    Containment is a measure of text similarity. It is the normalized, 
       intersection of ngram word counts in two texts.
        
    Arguments:
        param ngram_array: an array of ngram counts for an answer and source text.
    
    Returns: a normalized containment value.

    Note:   Function created as part of the plagiarism detection project 
            for udacities machine learning engineer nanodegree 
    '''
    
    # the intersection can be found by looking at the columns in the ngram array
    # this creates a list that holds the min value found in a column
    # so it will hold 0 if there are no matches, and 1+ for matching word(s)
    intersection_list = np.amin(ngram_array, axis=0)
    
    # optional debug: uncomment line below
    # print(intersection_list)

    # sum up number of the intersection counts
    intersection = np.sum(intersection_list)
    
    # count up the number of n-grams in the answer text
    answer_idx = 0
    answer_cnt = np.sum(ngram_array[answer_idx])
    
    # normalize and get final containment value
    containment_val =  intersection / answer_cnt

    return containment_val

# Calculate the ngram containment for one answer file/source file pair in a df
def calculate_containment(a_text, s_text, n):
    '''
    Calculates the containment between a given answer text and its associated source text.
    This function creates a count of ngrams (of a size, n) for each text file in our data.
    Then calculates the containmnet by finding the ngram count for a given answer text, 
    and its associated source text, and calculating the normalized intersection of those counts
    
    Arguments:
        df: a dataframe with columns 'File', 'Task', 'Category', 'Class', 'Text', and 'Datatype'
        n : an integer that defines the ngram size
        answer_filename: a filename for an answer text in the df ex 'g0pB_taskd.txt'
        
    Return: 
        A single containment value that represents the similarity between an answer text and its source text

    Note:   Function created as part of the plagiarism detection project 
            for udacities machine learning engineer nanodegree
    '''
     
    # calculate ngram_array
    ng_array =  ngram_array(a_text, s_text, n)
    
    # return containment
    return containment(ng_array)

def containment_wrapper(article_pair, n_gram_choice = 20):
    '''
    A wrapper around the calculate_containmnet function that accepts a list as input
    and performs error handling.

    Argument:
        article_pair    : (list) list containing two articles to comparse [articleA, article B]
        n_gram_choice   : an integer that defines the ngram size

    Returns:
        A single containment value that represents the similarity between the two articles
    '''

    try:
        containment = calculate_containment(article_pair[0], article_pair[1], n_gram_choice)
    except:
        print(f"We couldn't calculate the containment for row {article_pair[2]}")
        containment = None
    return containment

# Compute the normalized LCS given an answer text and a source text
def lcs_norm_word(answer_text, source_text):
    '''
    Computes the longest common subsequence of words in two texts; returns a normalized value.
        Arguments:
            answer_text: The pre-processed text for an answer text
            source_text: The pre-processed text for an answer's associated source text
        Returns: 
            A normalized LCS value

    Note:   Function created as part of the plagiarism detection project 
            for udacities machine learning engineer nanodegree
    
    '''
    
    # split text and find length
    A_split = answer_text.split()
    S_split = source_text.split()
    len_A = len(A_split)
    len_S = len(S_split)
    
    # initialise matrix
    lcs_matrix = np.zeros(shape = (len_S + 1, len_A + 1))
    
    # populate matrix
    for row in range(len_S):
        for col in range(len_A):
            # check equality of elements
            if A_split[col] == S_split[row]:
                # we have a match: add one to the top left diagonal cell
                lcs_matrix[row + 1, col + 1] = lcs_matrix[row, col] + 1
            else:
                # no match so take max of top and left cells
                lcs_matrix[row + 1, col + 1] = max(lcs_matrix[row + 1, col], lcs_matrix[row, col + 1])
    
    LCS = lcs_matrix[len_S, len_A]
    
    LCS_normalized = LCS / len_A
    
    return LCS_normalized

def lcs_wrapper(article_pair):
    '''
    A wrapper around the lcs_norm_word function that accepts a list as input
    and performs error handling.

    Argument:
        article_pair    : (list) list containing two articles to comparse [articleA, article B]

    Returns:
        A normalized LCS value
    '''

    try:
        LCS_normalized = lcs_norm_word(article_pair[0], article_pair[1])
    except:
        print(f"We couldn't calculate the longest common subsequence for row {article_pair[2]}")
        LCS_normalized = None
    return LCS_normalized