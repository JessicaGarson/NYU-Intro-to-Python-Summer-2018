# Advanced Loops
We're going to dig into some advanced concepts with loops today.

## Enumerate
Enumerate allows us to count when we use it with a list.

```python
attendees = ['Celestino', 'Yasha', 'Hamid']

for index, attendee in enumerate(attendees):
    print(index, attendee)
```

## Zip
Zip lets us tie to lists together in a loop.
```python
state_abvs = ['AK', 'AZ', 'MD']
state_names = ['Alaska', 'Arizona', 'Maryland']

for abv, name in zip(state_abvs, state_names):
    print('The abbrivation of {}, is {}.'.format(name, abv))
```
## Break
Break lets you exit out of a loop that would keep running for longer. The break statement causes a program to break out of a loop.

```python
number = 0

for number in range(10):
    number = number + 1

    if number == 5:

        break    # break here

    print('Number is {}'.format(number))

print('Out of loop')
```

## Continue
The continue statement gives you the option to skip over the part of a loop where an external condition is triggered, but to go on to complete the rest of the loop.

```python
number = 0

for number in range(10):
    number = number + 1

    if number == 5:

      continue   # continue here

    print('Number is {}'.format(number))

print('Out of loop')
```

## Pass
When an external condition is triggered, the pass statement allows you to handle the condition without the loop being impacted in any way; all of the code will continue to be read unless a break or other statement occurs.

As with the other statements, the pass statement will be within the block of code under the loop statement, typically after a conditional if statement.

```python
number = 0

for number in range(10):
    number = number + 1

    if number == 5:

        pass   # continue here

    print('Number is {}'.format(number))

print('Out of loop')
```

## +=
a += b is essentially the same as a = a + b, except that:

`+` always returns a newly allocated object, but += should (but doesn't have to) modify the object in-place if it's list or dict.

In a = a + b, a is evaluated twice.

age = 33
num = 13

Let's look at this example:

```python
age = 33
num = 13

while num < age:
    print(num)
```

This allows this code to keep iterating:

```python
while num < age:
    print(num)
    num += 1
```

Let's also look at this example:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## While True

While true allows the loop to run forever, unless there is a break noted:

```python
i = 0

while True:
    i += 1
    if i == 12:
        break
    print(i)
```
