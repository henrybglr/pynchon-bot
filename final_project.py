"""
File: final_project.py
------------------
Twitter bot that tweets a new character name every hour, compiled from the collected works
of Thomas Pynchon.
"""

import tweepy
import random
import time

CONSUMER_KEY = '(your key goes here)' # get your unique key from the twitter api
CONSUMER_SECRET = '(your key goes here)'
ACCESS_KEY = '(your key goes here)'
ACCESS_SECRET = '(your key goes here)'

# Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

INTERVAL = 60 * 60
# INTERVAL = 60  # for testing


def main():
    while True:
        name1 = first_name()
        name2 = last_name()
        api.update_status(name1 + ' ' + name2)
        time.sleep(INTERVAL)  # tweet once an hour


def first_name():  # returns random first name
    with open("PynchonFirstNames.txt") as f:
        lines = f.read().splitlines()
    return random.choice(lines)


def last_name():  # returns random last name
    with open("PynchonLastNames.txt") as f:
        lines = f.read().splitlines()
    return random.choice(lines)


# Boilerplate
if __name__ == '__main__':
    main()
