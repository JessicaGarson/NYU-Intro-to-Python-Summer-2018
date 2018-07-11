# Review
Functions can be a bit tricky so have no fear if you are having trouble right.

## What are Functions?
Functions are reusable bits of code. They allow us to repeat ourselves less and therefore prevent bugs.

Functions have the following:
- A def statement that allows us to define our function.
- A body of our code we can write our code in it.
- A return value - that gives us a value to save.

Functions take in parameters/arguments. Parameters are the variables inside the function. Arguments are the value passed into the function.

Here is a program that finds the square of a number.
```python
# Define the function
def square(x):  # Define the function
    """Returns the square of a number""" # Docstring
    y = x ** 2  # Body
    return y  # Return Statement


result = square(x=3)  # Call the function
print(result)  # Print out the result
````
In this example x is the variable inside of the function and therefore the parameter. 3 is the argument.

## Keyword Arguments
You can set keyword arguments in 2 different ways. One just calling the the function with the arguments. Or by setting the parameter equal to the argument.

```python
def plus(a,b):
  return a + b

plus(2,3)

plus(a=1, b=2)
```

## Local Variables
For the following function the variables area_code, second_part, and third part are local variables. Meaning they can't be called outside of the function.

```python
def number_formatted(phone_number):
    """Formats a phone number"""
    area_code = phone_number[0:3]
    second_part = phone_number[3:6]
    third_part = phone_number[6:]
    return '({})-{}-{}'.format(area_code, second_part, third_part)


# print(second_part)
print(number_formatted(phone_number="3017041328"))
```

## Global Scope
In the example below since 6 was assigned outside a function it is in the local scope and we call in the global variable so that we can make changes to it in our program as a whole.


```python
a = 6


def oneplus():
    global a
    a = 1 + a
    return a


def twoplus():
    global a
    a = 2 + a
    return a


print(a)
print(oneplus())
print(twoplus())
print(a)
```

## Variables Can Have The Same Names

You can have 2 different variables in two different functions that have the same name.

```python
def hello():
    name = 'Jess'
    return 'Hello {}'.format(name)


def hi():
    name = 'Alex'
    return 'Hi {}'.format(name)


print(hi())
print(hello())
```

## The Main Function Tying It All Together
The main function allows us to tie everything together and make our code a bit more readable.

```python
name = str(input('Enter your name: '))
print('The name you entered is {}'.format(name))


# Define function to check if name contains a vowel
def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')


# Define main method that calls other functions
def main():
    has_vowel()


# Execute main() function
if __name__ == '__main__':
    main()
```

We also have some code at the end which tells our code to run. In Python, '__main__' is the name of the scope where top-level code will execute. When a program is run from standard input, a script, or from an interactive prompt, its __name__ is set equal to '__main__'.

```
if __name__ == '__main__':
    # Code to run when this is the main program here.
```

## Another Option Without the Main Function

We can also run this program without the main function like this. We also added some of the main instruction to the name block as well.

```python
# Define function to check if name contains a vowel
def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')


if __name__ == '__main__':
    name = str(input('Enter your name: '))
    print('The name you entered is {}'.format(name))
    has_vowel()
```

## Homework One with Functions

Let's talk through this version of our first homework assignment.

```python
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

What can be made better about this code? It works but there are some awkward things about it. What is awkward about it?

Let's take a look at the variables in the main function these can be made better? How so?

## Homework 2 Solutions
Let's talk through solutions to homework two. What worked well? What didn't? How would we solve these problems.
