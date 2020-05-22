"""
File: final_project.py
------------------
Twitter bot that tweets a new character name every hour, compiled from the collected works
of Thomas Pynchon.
"""

import tweepy
import random
import time

CONSUMER_KEY = 'SWvH0XEAEktPtvujC6xi453jp'
CONSUMER_SECRET = 'LUTtjsx6MWQd6uE6D9O8kJtO6Jvl1vs6oMEFQbQFMVJiyk9pOy'
ACCESS_KEY = '1253125310691901440-87t2Lv2BqccS8D2pGRXyoZiry1XHMs'
ACCESS_SECRET = 'kz4rxqKb9ieHMJVj466uwzejRLX6uUbmECpKj3omxl7o4'

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
