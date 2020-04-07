'''
get_poll.py: grab a random poll
7 Apr 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

from polls import POLL


def get_poll():
    poll_to_tweet = choice(POLL)

    return poll_to_tweet
