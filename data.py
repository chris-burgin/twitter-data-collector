import MySQLdb


class Data():
    def __init__(self):
        self.db = MySQLdb.connect(host="127.0.0.1",
                                  user='root',
                                  passwd='',
                                  db='Twitter_Data')

        self.cur = self.db.cursor()

    # Tweets
    def AddTweet(self, tweet_id, tweet, userid):
        if self.TweetExists(tweet_id) == False:
            self.cur.execute(
                                """
                                    INSERT INTO tweets (tweet_id, tweet, userid)
                                    VALUES (%s, %s, %s)
                                """,
                                (tweet_id, tweet, userid)
                            )

            self.db.commit()
            return True
        else:
            return False

    def TweetExists(self, tweet_id):
        data = self.cur.execute(
                                    """
                                        SELECT  tweet_id
                                        FROM    tweets
                                        WHERE   tweet_id = '%s'
                                    """,
                                    (tweet_id,)
                               )
        if data > 0:
            return True
        else:
            return False

    # Users
    def FetchUsers(self):
        self.cur.execute(
                            """
                                SELECT  *
                                FROM    users
                            """
                        )
        data = self.cur.fetchall()
        return data

    def SetUserID(self, screenname, userid):
        self.cur.execute(
                            """
                                UPDATE  users
                                SET     userid = %s
                                WHERE   screenname = %s
                            """,
                            (userid, screenname)
                        )

        self.db.commit()
