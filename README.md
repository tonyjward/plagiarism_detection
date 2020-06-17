# Plagiarism Detection
The aim of this project is to use machine learning to identify plagiarism in articles written about data science on the Medium platform. Here are some examples flagged by our model.

* **Logistic Regression:** [Article A](https://towardsdatascience.com/why-linear-regression-is-not-suitable-for-binary-classification-c64457be8e28?source=search_post) vs [Article B.](https://medium.com/@elenjubbas/linear-regression-vs-logistic-regression-for-classification-tasks-b42f85487857?source=search_post)

* **Naive Bayes:** [Article A](https://medium.com/@mahjahnavi/natural-language-processing-an-overview-of-key-algorithms-and-their-evolution-2d9612d1f764?source=search_post) vs [Article B.](https://medium.com/reality-engines/natural-language-processing-an-overview-of-key-algorithms-and-their-evolution-3588d2cef90f?source=search_post)

* **Random Forest:** [Article A](https://medium.com/datadriveninvestor/ensemble-learning-and-random-forest-7430ebf3da7e?source=search_post) vs [Article B.](https://medium.com/@Synced/how-random-forest-algorithm-works-in-machine-learning-3c0fe15b6674?source=search_post)

* **Xgboost:** [Article A](https://towardsdatascience.com/boosting-performance-with-xgboost-b4a8deadede7?source=search_post) vs [Article B.](https://medium.com/@knoldus/machinex-boosting-performance-with-xgboost-28c9f49998a6?source=search_post)

More examples can be found in the [results section](notebooks/2_investigate_plagiarism.ipynb)

# How I did it
## Source Data
Researchers at the University of Sheffield created a corpus in which plagiarism has been simulated:

>Plagiarism is widely acknowledged to be a significant and increasing problem for higher education institutions. To test and develop systems to detect plagiarism, evaluation resources are required. To address this, we created a corpus consisting of short (200-300 words) answers to Computer Science questions in which plagiarism has been simulated. The corpus has been designed to represent varying degrees of plagiarism and we envisage will be a useful addition to the set of resources available for the evaluation of plagiarism detection systems. Although a small collection of plagiarised texts, this corpus has been systematically created and we hope will provide a 'blueprint' for the construction of further resources.

> **Citation for data**: Clough, P. and Stevenson, M. Developing A Corpus of Plagiarised Short Answers, Language Resources and Evaluation: Special Issue on Plagiarism and Authorship Analysis, In Press. [Download](https://ir.shef.ac.uk/cloughie/resources/plagiarism_corpus.html)

An exploration of the data can be found [here](udacity/Solutions/1_Data_Exploration.ipynb)

## Modelling

As part of the Machine Learning Nanodegree I used the above data to build a binary classifier that could distinguish between plagiarised and non-plagiarised answers. 
during the [feature engineering stage](udacity/Solutions/2_Plagiarism_Feature_Engineering.ipynb) I calculated two similarity metrics which were used to compare each students answers to the source text.
1) Containment
2) Longest Commmon Subsequcne

TBC: SHOW IMAGE

Next I used Amazon Sagemaker and PyTorch to create a single layer feed forward network [that achieved 96% accuracy, 100% precision and 94% recall on a test set.](udacity/Solutions/3_Training_a_Model.ipynb)

## Application to Medium Articles
Throughout the project I was itching to apply the techniques to another "real life" dataset. I thought the content sharing platform Medium would provide a rich source of data - and decided to look for plagiarism in articles written about data science. In order to do this I build a web scraper using a combination of Selelium and Beautiful soup that could log in to Medium using a twitter handle (you need a paid subscription to access all the articles) and download all articles for a specific search term. I compared the articles pairwise, ranked them and brought back the top 5 most likely article combinations to contain plagiarism.

#### -- Project Status: Under Development

### Methods Used
* Webscraping (Selenium, Beautiful Soup)
* Optimisation (OLS, Gradient Descent, Particle Swarm)

### Technologies
* Python

### Tests
Tests can be run from the main directory using
```
python -m unittest discover
```

## Contact
* tony@statcore.co.uk



# Instructions

first run this
`sudo docker run -d --rm --name standalone-firefox -p 4444:4444 -p 5900:5900 --shm-size 2g selenium/standalone-firefox-debug:3.141.59`
to start a selenium server

run using
`./scrape_data.sh '[logistic regression,naive bayes]' data`

Then scale up the machine

`./check_plagiarism.sh '[logistic regression,naive bayes]' data`
