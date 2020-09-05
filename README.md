# Disable Advertisers
_Stefan Arentz, September 2020_

This Python script reads in a `twitter_advertiser_list.pdf`, extracts all the screen names from it and then mutes those. Unclear how effective this is.

The `twitter_advertiser_list.pdf` can be requested from your Twitter profile settings Mine contained a list of 2200 screen names.

```
$ export CONSUMER_KEY=...
$ export CONSUMER_SECRET=...
$ export ACCESS_TOKEN=...
$ export ACCESS_TOKEN_SECRET=...
$ ./mute-advertisers.py twitter_advertiser_list.pdf
```

