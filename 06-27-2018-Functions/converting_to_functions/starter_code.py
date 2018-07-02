twitter_max = input("What is the maximum number of characters permitted in twitter posts?\n")

tweet = input("What would you like to tweet?\n")

len_tweet = len(tweet)
print(len_tweet)

len_allowed = int(twitter_max)
len_remain = len_allowed - len_tweet

if len_remain <= len_allowed:
    print('That tweet is {} characters and you have {} remaining characters' .format(len_tweet, len_remain))
else:
    print('That tweet is {} characters and you have to trim by {} characters').format(len_tweet, - len_remain)
