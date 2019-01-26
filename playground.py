import pandas as pd 
import numpy as np

# data1 = pd.read_csv("red-wine-set.zip")
# data2 = pd.read_csv("ks-projects-201801.csv")

# print data2.head
# print data1.head
# print data1

# quality = data1["quality"].values
# print quality

# Display the first five records
# display(data1.head(n=5))

# display(np.round(data1.describe()))
# pd.plotting.scatter_matrix(data1, alpha = 0.3, figsize = (40,40), diagonal = 'kde')
# plt.show()




from bs4 import BeautifulSoup
import requests
# with open('greatwebsite.html') as html_file:
#     guy = BeautifulSoup(html_file, 'lxml')

# match = guy.title.text
# print(match)


import json
import csv
import tweepy
import re


def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)
    
    #get the name of the spreadsheet we will write to
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    #open the spreadsheet we will write to
    with open('%s.csv' % (fname), 'w') as file:

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(('timestamp', 'favorite_count', 'retweet_count', 'tweet_text', 'username'))

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                   lang="en", tweet_mode='extended').items(100):

            w.writerow((tweet.created_at, 
                        tweet.favorite_count,
                        tweet.retweet_count,
                        tweet.full_text.replace('\n',' '), 
                        tweet.user.screen_name))

consumer_key = 'ntTWxIY044YXyJMF02vTCDnAT'
consumer_secret = 'k7BdSBN7boMmTZs0ARBInDzcIW2iBDydwWvfywPfNhxIhCqcWo'
access_token = '2397220466-hOqEPqYrL7WKSu0n72eCJPCu7BuMfEGrPWCDaIs'
access_token_secret = 'VSKJEvMqXoROI27ryHSVIGDJH3fhLarEUUrLL8c1KJ38c'
    
hashtag_phrase = '#slacklogo'

search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)


# 1. Choose product (Shell, Slack, Microsoft, Uber/Lyft, Nike/Adidas, Nintendo, Tesla, Kellogg) (Tweets versus election cycle)
# 2. Scrape data
# 3. Implement sentiment analysis 
# 4. See results ... ?
# 5. Intent analysis
# 6. CSS/


# correlation = data1.corr()
# # display(correlation)
# plt.figure(figsize=(14, 12))
# heatmap = sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")
# plt.show()




# import time, sys, threading
# from datetime import timedelta, date
# # install selenium https://pypi.python.org/pypi/selenium
# from selenium import webdriver
# # make sure geckodriver is in the PATH

# # change the date here, 1 keyword a thread/browser
# keywords = ['McMurtry']
# # change the date here, 1 day a thread/browser
# # No. browsers opened = No. keywords * No. days
# start_year = 2018
# start_month = 12
# start_day = 6
# end_year = 2018
# end_month = 12
# end_day = 7

# # twitter required params
# login_url = 'https://www.twitter.com/login'
# base_url = 'https://twitter.com/search?q='
# since = '%20since%3A'
# until = '%20until%3A'
# src = '&src=typd'
# time_sleep = 5
# js_scroll_down = 'window.scrollTo(0, document.body.scrollHeight);'

# # new file header
# file_header = 'tweets-'


# def daterange(start_date, end_date):
#     for n in range(int ((end_date - start_date).days)):
#         yield start_date + timedelta(n)

# def getTweet(keyword, start_date, end_date):
# 	# please create files for storing credentials
# 	MY_SCREEN_NAME = open('username.txt').read().strip()
# 	MY_PASSWORD = open("password.txt").read().strip()
# 	# please remove encoding argument if using Mac
# 	ftweets = open('{}_{}_{}_{}'.format(file_header,keyword,start_date,end_date),'w')
# 	browser = webdriver.Firefox()
# 	browser.get(login_url)
# 	time.sleep(time_sleep)

# 	username = browser.find_element_by_class_name("js-username-field")
# 	username.send_keys(MY_SCREEN_NAME)
# 	password = browser.find_element_by_class_name("js-password-field")
# 	password.send_keys(MY_PASSWORD)

# 	query = keyword + since + start_date + until + end_date + src
# 	url = base_url + query

# 	browser.get(url)
# 	time.sleep(time_sleep)

# 	while True:
# 		time.sleep(time_sleep)
# 		target_set = set()
# 		browser.execute_script(js_scroll_down)
# 		body = browser.find_element_by_class_name('stream')
# 		tweets = browser.find_elements_by_class_name('tweet-text')
# 		for tweet in tweets:
# 			ftweets.write('{}{}'.format(tweet.text,'\n'))

# start_date = date(start_year, start_month, start_day)
# end_date = date(end_year, end_month, end_day)

# for i in range(len(keywords)):
# 	for rank, single_date in zip(range((end_date-start_date).days), daterange(start_date, end_date)):
# 		current_date = single_date.strftime('%Y-%m-%d')
# 		y,m,d = current_date.split('-')
# 		next_date = (date(int(y), int(m),int(d))+timedelta(1)).strftime('%Y-%m-%d')
# 		y_n, m_n, d_n = next_date.split('-')
# 		p = threading.Thread(target=getTweet, args=(keywords[i], current_date, next_date))
# 		p.start()