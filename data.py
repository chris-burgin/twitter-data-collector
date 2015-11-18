import MySQLdb


class Data():
    def __init__(self):
        self.db = MySQLdb.connect(host="127.0.0.1",
                                  user='root',
                                  passwd='',
                                  db='Twitter_Data')
        self.cur = self.db.cursor()

    # Tweets
    def AddTweet(self, tweetid, tweet, userid):
        if self.TweetExists(tweetid) is False:
            self.cur.execute("""
                                INSERT INTO tweets (tweetid, tweet, userid)
                                VALUES (%s, %s, %s)
                             """, (tweetid, tweet, userid)
                             )
            self.db.commit()
            return True
        else:
            return False

    def TweetExists(self, tweetid):
        data = self.cur.execute("""
                                    SELECT  tweetid
                                    FROM    tweets
                                    WHERE   tweetid = '%s'
                                """, (tweetid,)
                                )
        if data > 0:
            return True
        else:
            return False

    def FetchUnParsedTweets(self):
        self.cur.execute("""
                            SELECT  *
                            FROM    tweets t
                            WHERE   t.parsed = 0
                         """
                         )
        data = self.cur.fetchall()
        return data

    def ParsedTweet(self, tweetid):
        self.cur.execute("""
                            UPDATE  tweets
                            SET     parsed = 1
                            WHERE   tweetid = %s
                         """, (tweetid,)
                         )
        self.db.commit()

    # Users
    def FetchUsers(self):
        self.cur.execute("""
                            SELECT  *
                            FROM    users
                         """
                         )
        data = self.cur.fetchall()
        return data

    def SetUserID(self, screenname, userid):
        self.cur.execute("""
                            UPDATE  users
                            SET     userid = %s
                            WHERE   screenname = %s
                         """, (userid, screenname)
                         )
        self.db.commit()

    def AddWord(self, tweetid, word):
        self.cur.execute("""
                            INSERT INTO words (tweetid, word)
                            VALUES (%s, %s)
                         """, (tweetid, word)
                         )
        self.db.commit()
