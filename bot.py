for submission in submissions:
                if submission['data']['is_self'] and submission['data']['id'] not in submitted:
                    sleep(self.options.submit_rate)
                    self.submit(submission['data'], modhash)
