# Review

## Lists
- Lists are containers that can hold multiple pieces of information.
- Lists are commonly used to hold strings (ex: list of attendees’ names) or numbers (ex: number of attendees for each class)
- Lists are a data structure that allows us to hold multiple values.
- Lists are are created by placing items inside of [ ] 
- They are comma separated

```python
favorite_foods = ['pizza', 'ice cream', 'cake']
```

## Loops
- Using loops we can automate and repeat tasks in a very short amount of time.

## For Loops
- A for loop lets you use each item one at a time, which is great for performing actions a certain number of times.

```python
favorite_foods = ['pizza', 'ice cream', 'kale']

for food in favorite_foods:
    print(food)
```

```python
forth_plans = ['seeing fireworks', 'a bbq', 'a concert']

for plan in forth_plans:
    print('My plans for July 4th were {}'.format(plan))
```

## While Loops
- While loops are the cousins of conditionals.
- While loops are repeating conditional statements. After an if statement, the program continues to execute code, but in a while loop, the program jumps back to the start of the while statement until the condition is False. Think about Eddie and Jess and the mints.

```python
temperature = 115

while temperature > 112:
    print(temperature)
    temperature = temperature - 1

print('The tea is cool enough.')
```
