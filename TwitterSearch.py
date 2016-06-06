# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 12:18:45 2016

@author: dvalentin
"""

import TwitterSearch

affiliates = ["Acadian", "Barrow Hanley Mewhinney & Strauss LLC", "Campbell Global", "Copper Rock Capital Partners", "Heitman", "Investment Counselors of Maryland LLC"]

def main():
    pass    

def search():
    
    try:
        tso = TwitterSearch.TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords(['', 'Doktorarbeit']) # let's define all words we would like to have a look for
        tso.set_language('de') # we want to see German tweets only
        tso.set_include_entities(False) # and don't give us all those entity information
    
        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key = 'aaabbb',
            consumer_secret = 'cccddd',
            access_token = '111222',
            access_token_secret = '333444'
         )
    
         # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
    
    except TwitterSearch.TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)
        

    
if __name__ == "__main__":
    main()
else:
    print("File is being imported")