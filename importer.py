import tweepy
import time
from data import Data


class Importer():

    def __init__(self):
        consumer_key = 'JOrMVul16BD5CZqmBj1Cu4xKc'
        consumer_secret = 'dbBEX9YPMCT0HwY1majuAZImNS0zQLye2U72sP57a8TdfI6kCS'

        access_token = '392213214-w4tgIG5EHii7e6Em8piYppSYRf4LPSY1u2nSM3Yt'
        access_token_secret = 'h6wD1Gui4rUih6nbViezi8Vt8r9b74ayYpUc6ZbYpydxw'

        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(self.auth)

    def ParseUsers(self):
        userids = []
        for user in data.FetchUsers():
            userids.append(user[1])
        return userids

    def UpdateUserIds(self):
        for user in data.FetchUsers():
            screenname = user[2]
            userid = self.api.get_user(screen_name=screenname).id
            data.SetUserID(screenname, userid)

    def ImportTweets(self, userids):
        for userid in userids:
            tcursor = tweepy.Cursor(self.api.user_timeline, user_id=userid)
            for item in tcursor.items():
                print(item.id)
                try:
                    if data.AddTweet(item.id, item.text,
                                     item.user.id) is False:
                        break
                except:
                    pass

                time.sleep(.3)

    def ParseTweets(self):
        for tweet in data.FetchUnParsedTweets():
            for word in tweet[2].split():
                data.AddWord(tweet[1], word)

            data.ParsedTweet(tweet[1])

# Objects
data = Data()
importer = Importer()

# Main
# Update User Screen Names
# importer.UpdateUserIds()

# Gets Users
# users = importer.ParseUsers()

# Imports New Tweets
# importer.ImportTweets(users)

# Parse Tweet
print('starting parsing')
importer.ParseTweets()
