# Plagiarism Detection
During the Udacity Machine Learning Nanodegree I built a plagiarism detector that examines a text file and performs binary classification; labeling that file as either plagiarized or not, depending on how similar the text file is when compared to a provided source text.
> **Citation for data**: Clough, P. and Stevenson, M. Developing A Corpus of Plagiarised Short Answers, Language Resources and Evaluation: Special Issue on Plagiarism and Authorship Analysis, In Press. [Download]

I used PyTorch to create a single layer feed forward network that achieved 96% accuracy, 100% precision and 94% recall on a test set.

Throughout the project I was itching to apply the techniques to another "real life" dataset. I thought the content sharing platform Medium would provide a rich source of data - and decided to look for plagiarism in articles written about data science. In order to do this I build a web scraper using a combination of Selelium and Beautiful soup that could log in to Medium using a twitter handle (you need a paid subscription to access all the articles) and download all articles for a specific search term. I compared the articles pairwise, ranked them and brought back the top 5 most likely article combinations to contain plagiarism.

Here is what I found

* [Xgboost](https://github.com/tonyjward/machine-learning-oop/blob/master/twlearn/LinearRegression.py) - identical article posted under two usernames
* [Random Forest](https://github.com/tonyjward/machine-learning-oop/blob/master/twlearn/GradientDescent.py) - more deceptive plagiarism with paraphrasing

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
