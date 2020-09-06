#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/


#
# Usage:
#
#  $ export CONSUMER_KEY=...
#  $ export CONSUMER_SECRET=...
#  $ export ACCESS_TOKEN=...
#  $ export ACCESS_TOKEN_SECRET=...
#  $ ./block-advertisers.py twitter_advertiser_list.pdf
#
# See https://github.com/st3fan/block-advertisers
#


import os, sys, time

from pdfminer.high_level import extract_text
from twython import Twython


CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


if __name__ == "__main__":

    text = extract_text(sys.argv[1])
    users = [line[1:] for line in text.split("\n") if line.startswith("@")]

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    for user in users:
        print(f"[*] Blocking @{user}")
        try:
            twitter.create_block(screen_name=user, include_entities=False, skip_status=True)
        except Exception as e:
            print(f"[!] Failed to block @{user}: {str(e)}")
        time.sleep(5)

