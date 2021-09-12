import praw

reddit = praw.Reddit('Cummy')

subreddit = reddit.subreddit("botte1t")

for submission in subreddit.hot(limit=8):
                if submission['data']['is_self'] and submission['data']['id'] not in submitted:
                    sleep(self.options.submit_rate)
                    self.submit(submission['data'], modhash)
