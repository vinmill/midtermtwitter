# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv
# Creating list to append tweet data 
df = pd.DataFrame(columns=['Datetime', 'Tweet Id', 'Text', 'Username','replyCount','retweetCount','likeCount','quoteCount','retweetedTweet','quotedTweet', 'State', 'Party'])
# Using TwitterSearchScraper to scrape data and append tweets to list
indy = 0
def scraper(user, num):
    global df, indy
    tweets_list1 = []
    username = user[0].replace('@','')
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:' + str(username) + ' since:2021-10-01 until:2022-10-01').get_items()): #declare a username 
        if i>num: #number of tweets you want to scrape
            break
        tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.retweetedTweet, tweet.quotedTweet, user[1], user[2]]) #declare the attributes to be returned
        
    # Creating a dataframe from the tweets list above 
    tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username','replyCount','retweetCount','likeCount','quoteCount','retweetedTweet','quotedTweet', 'State', 'Party'])
    df = pd.concat([tweets_df1, df], axis=0)
    indy += 1
    print('sen: ' + str(indy))
 
# opening the CSV file
with open('twitterusers.csv', mode ='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        scraper(lines, 5000)
df.sort_values(by=['Party','Username','likeCount', 'Datetime']).reset_index(drop=True)
df.to_csv('tweets.csv')