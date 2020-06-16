import re

def remove_junk(article_raw, first_break = 'Written by', second_break = 'Follow'):
    '''
    Removes unncessary text found at bottom of article such as links
    to other articles
    
    Arguments:
        article_raw: (str) raw article text
        first_break: where to make first break in text
        second_break: where to make second break in text
    
    Returns:
        (author, article, junk) splits out article text vs junk text
    '''
    
    if ('Written by' not in article_raw) or ('Follow' not in article_raw):
        author = "Blank"
        article = "Blank"
        junk = article_raw
    else:
        # split main article vs everything else
        first_position = re.search(first_break, article_raw)
        article = article_raw[:first_position.start()]
        everything_else = article_raw[first_position.start():]
        
        # split everything else into author and junk
        second_position = re.search(second_break, everything_else)
        author = everything_else[len('Written by'):second_position.start()]
        junk = everything_else[second_position.start():]
    
    return (author, article, junk)

def clean_articles(articles_raw):
    '''
    Removes junk text from a list of articles
    
    Arguments:
        articles_raw: list of raw article text
        
    Returns:
        articles_clean: 
    '''

    return [remove_junk(article) for article in articles_raw]
        
