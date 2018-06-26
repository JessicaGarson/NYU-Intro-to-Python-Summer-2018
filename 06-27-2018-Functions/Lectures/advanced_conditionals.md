# Advanced Conditionals

## Questions
We will be holding all questions to the end.

## Comments
Comments are code that doesn't run.

```python
# I am a comment, I don't run
print('hello world!')
```

# Advanced Conditionals
We're going to dive into some advanced uses of conditionals

## In
The in keyword, when used with a conditional, tells you whether some text appears in a string.

```python
if 'Messica Arson' in article:
    print('It is so awesome Jess got her DJ project in this article')
```

## And  
Using the and keyword, both conditions must be true for the print statement to run.

```python
homework_assigned = 1
homework_turned_in = 0

if homework_turned_in == 0 and homework_assigned == 1:
    print('Jess is sad')
```

```python
grade = 80

if grade >= 90 and grade <= 100:
    print("You got a A")
elif grade >= 80 and grade <= 89:
    print("You got a B")
elif grade >= 70 and grade <= 79:
    print("You got a C")
elif grade >= 60 and grade <= 69:
    print("You got a D")
else:
    print("I'm sorry to say you failed this class")
```

## Or
Using the or keyword, either condition could be true for the print statement to run.
```python
if state == 'MD' or state == 'DC' or state == 'DE' or state == 'VA' or state == 'PA':
  print('You are from the Mid-Atlantic region')
```

## Nested Conditionals
You can nest conditions into other conditions.

```python
state = 'CA'

if state == 'NY':
    print('You are in NY, it should be a short drive')
elif state == 'NJ':
    print('You are in NJ, come visit us if you can')
elif state == ('CT'):
    print('You are in CT, come visit us if you can')
else:
    print('We only service the New York Region')

    if state == 'PA':
        print('You are welcome to visit us still')
    elif state == 'CA':
        print('Wow, that would be quite the drive')
```

## Questions
Any questions you may have.
