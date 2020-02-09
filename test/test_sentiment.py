import matplotlib.pyplot as plt
from mock import patch, Mock
import numpy as np
import pandas as pd
import pandas.core.base
from pandas.core.base import IndexOpsMixin
import pandas.core.frame
from pandas.core.frame import BlockManager
import pandas.core.generic
from pandas.core.generic import BlockManager
import re
from re import Scanner
from textblob import TextBlob
import textblob.blob
from textblob.blob import BaseBlob
import textblob.decorators
from textblob.decorators import cached_property
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy.api
from tweepy.api import API
import tweepy.auth
from tweepy.auth import API
import tweepy.binder
from tweepy.streaming import StreamListener
import unittest

from src.sentiment import TweetAnalyzer
from src.sentiment import TwitterAuthenticator
from src.sentiment import TwitterClient




class SentimentTest(unittest.TestCase):

    @patch.object(OAuthHandler, 'set_access_token')
    @patch.object(OAuthHandler, '__init__')
    def test_authenticate_twitter_app(self, mock___init__, mock_set_access_token):
        mock___init__.return_value = None
        mock_set_access_token.return_value = None
        twitterauthenticator_instance = TwitterAuthenticator()
        self.assertIsInstance(
            twitterauthenticator_instance.authenticate_twitter_app(),
            tweepy.auth.OAuthHandler
        )


    @patch.object(re, 'sub')
    def test_clean_tweet(self, mock_sub):
        mock_sub.return_value = u''
        tweetanalyzer_instance = TweetAnalyzer()
        self.assertEqual(
            tweetanalyzer_instance.clean_tweet({}),
            u''
        )


    def test_get_twitter_client_api(self):
        twitterclient_instance = TwitterClient(None)
        self.assertIsInstance(
            twitterclient_instance.get_twitter_client_api(),
            tweepy.API
        )


    @patch.object(pd.DataFrame, '__setitem__')
    @patch.object(pd.DataFrame, '__init__')
    def test_tweets_to_data_frame(self, mock___init__, mock___setitem__):
        mock___init__.return_value = None
        mock___setitem__.return_value = None
        tweetanalyzer_instance = TweetAnalyzer()
        self.assertIsInstance(
            tweetanalyzer_instance.tweets_to_data_frame([]),
            pandas.core.frame.DataFrame
        )


if __name__ == "__main__":
    unittest.main()