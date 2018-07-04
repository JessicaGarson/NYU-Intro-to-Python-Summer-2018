# Guide to turning your homework into having functions
We will go through how to turn a program that was written without functions into one with functions.

## Starter code
The code we are starting with for this guide is as follows:

```python
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
```

## Create a new file in Atom
Let's call it `tweet_length_functions.py`

## Start with boiler plate
At the bottom of the new file start with the following boiler plate code:

```python
if __name__ == '__main__':
    main()
```

## Create the framework for the main function
To start things off let's create a main function right above the boiler plate we just added

```python
def main():
```

## Let's create our first function
The starter code for our program asks the current max characters for twitter. Let's turn that into a function.

```python
def max_tweet():
    return input("What is the maximum number of characters permitted in twitter posts?\n")
```

Now let's add the function call to the main function so it looks like this:

```python
def main():
    tweet_length = max_tweet()
````

Save your file and inside the command line run:

```bash
python tweet_length_functions.py
```
## Let's convert your string into an integer
Because the input function automatically returns a string object. You will need to convert this into an integer so you can use it to do math.

Let's create a function that does this:

```python
def convert_int(twitter_max):
    return int(twitter_max)
```

Now let's add this function call into our main function. Our main function should now look like this:

```python
def main():
    tweet_length = max_tweet()
    int_tweet_max = convert_int(twitter_max=tweet_length)
```

Save your file and inside the command line run:

```bash
python tweet_length_functions.py
```

## Let's ask the user what to tweet
Let's create a function that asks the user what tweet:

```python
def tweet():
    return input("What would you like to tweet?\n")
```

Let's add this to our main function so it now looks like this:

```python
def main():
    tweet_length = max_tweet()
    int_tweet_max = convert_int(twitter_max=tweet_length)
    what_to_tweet = tweet()
```

Save your file and inside the command line run:

```bash
python tweet_length_functions.py
```

## We'll need to grab the length of this tweet
So let's create a function that has the following:

```python
def tw_length(tweet):
    return len(tweet)
```

We'll need to pass in the tweet as an argument here so we can see how long it is.

Now let's add the function call to our main function, so it now looks as follows:

```python
def main():
    tweet_length = max_tweet()
    int_tweet_max = convert_int(twitter_max=tweet_length)
    what_to_tweet = tweet()
    tweet_length = tw_length(tweet=what_to_tweet)
```

Save your file and inside the command line run:

```bash
python tweet_length_functions.py
```

## How many characters do you have remaining
Let's create a function that does the math of how many characters you have remaining so you will need the length allowed and the length remaining. We'll create a function that does this simple subtraction here.

```python
def remain(len_allowed, len_tweet):
    return len_allowed - len_tweet
```

Let's now add this into our to our main function:

```python
def main():
    tweet_length = max_tweet()
    int_tweet_max = convert_int(twitter_max=tweet_length)
    what_to_tweet = tweet()
    tweet_length = tw_length(tweet=what_to_tweet)
    len_remain = remain(len_allowed=int_tweet_max, len_tweet=tweet_length)
    logic(len_allowed=int_tweet_max, len_remain=len_remain)
```

Save your file and inside the command line run:

```bash
python tweet_length_functions.py
```

## Now let's add in the logic
To add in the core of our starter program which is the if/else statement let's create a function called logic for this:

```python
def logic(tweet_length, len_allowed, len_remain):
    if len_remain <= len_allowed:
        print('That tweet is {} characters and you have {} remaining characters'.format(tweet_length, len_remain))
    else:
        print('That tweet is {} characters and you have to trim by {} characters'.format(len_allowed, len_allowed - len_remain))
```

Now let's update the main function so it now looks like this:

```python
def main():
    tweet_length = max_tweet()
    tweet_length_int = convert_int(tweet_length)
    what_to_tweet = tweet()
    tweet_length = tw_length(tweet=what_to_tweet)
    len_remain = remain(len_allowed=tweet_length_int, len_tweet=tweet_length)
    logic(tweet_length=tweet_length, len_allowed=tweet_length_int, len_remain=len_remain)
```

Save your file and inside the command line run:

```bash
python tweet_length_functions.py
```

And you should see that your program works!

## Full code
The full code should look as follows:

```python
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


def logic(tweet_length, len_allowed, len_remain):
    if len_remain <= len_allowed:
        print('That tweet is {} characters and you have {} remaining characters'.format(tweet_length, len_remain))
    else:
        print('That tweet is {} characters and you have to trim by {} characters'.format(len_allowed, len_allowed - len_remain))


def main():
    tweet_length = max_tweet()
    tweet_length_int = convert_int(tweet_length)
    what_to_tweet = tweet()
    tweet_length = tw_length(tweet=what_to_tweet)
    len_remain = remain(len_allowed=tweet_length_int, len_tweet=tweet_length)
    logic(tweet_length=tweet_length, len_allowed=tweet_length_int, len_remain=len_remain)


if __name__ == '__main__':
    main()

```
