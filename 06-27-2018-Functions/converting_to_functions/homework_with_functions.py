# We will add in our new version of the homework


def max_tweet():
    return input("What is the maximum number of characters permitted in twitter posts?\n")


def convert_int(twitter_max):
    return int(twitter_max)


def tweet():
    return input("What would you like to tweet?\n")


def tw_length(tweet):
    return len(tweet)


def remain(len_allowed, len_tweet):
    return len_allowed - len_tweet


def logic(len_allowed, len_remain):
    if len_remain <= len_allowed:
        print('That tweet is {} characters and you have {} remaining characters'.format(len_allowed, len_remain))
    else:
        print('That tweet is {} characters and you have to trim by {} characters'.format(len_allowed, len_allowed - len_remain))


def main():
    tweet_length = max_tweet()
    int_tweet_max = convert_int(twitter_max=tweet_length)
    what_to_tweet = tweet()
    tweet_length = tw_length(tweet=what_to_tweet)
    len_remain = remain(len_allowed=int_tweet_max, len_tweet=tweet_length)
    logic(len_allowed=int_tweet_max, len_remain=len_remain)


if __name__ == '__main__':
    main()
