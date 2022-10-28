import snscrape.modules.twitter as sntwitter
import pandas as pd

dfin = pd.read_csv('tweets.csv')
dfin = dfin[dfin.quotedTweet == None]
dfin = dfin[dfin.retweetedTweet == None]
pd.display(dfin)