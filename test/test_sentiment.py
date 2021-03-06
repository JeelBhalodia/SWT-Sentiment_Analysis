from mock import patch
import pandas as pd
import pandas.core.base
import pandas.core.frame
import pandas.core.generic
import re
from tweepy import OAuthHandler
import tweepy.api
import tweepy.auth
import tweepy.binder
import unittest

from sentiment import TweetAnalyzer
from sentiment import TwitterAuthenticator
from sentiment import TwitterClient

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