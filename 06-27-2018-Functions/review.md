# Review

## Variables
Variables are containers of information that we can call.

## Data Types in Python
There are three data types in Python
- Integers such as 1, 23, -32, 24, 234
- Floating point numbers or floats such as 1.23, 23.23, -4.32, 22.6
- Strings such as 'rwewe', '2si', 'hello', 'anything really', you can spot a string by the quotes around it.

## Booleans
Statements that evaluate down to true or false.

```python
3 == 2
4 >= 3
6 < 6
8 != 9
```

## Slicing
Slicing allows us to get pieces of a string.

```python
phone_number = '2022343259'
area_code = phone_number[0:3]
middle_part = phone_number[3:6]
last_part = phone_number[6:]
```

## String Formatting
String formatting allows us to interject variables into strings.

```python
formatted_number = "({}){}-{}".format(area_code, middle_part, last_part)
print(formatted_number)
```

## But Jess, I saw a different way, why your way?
There are many different ways to do string formatting. I teach with `.format()` because this is the way that I use when I write code. The wonderful thing about code is that there isn't one right answer.

Another common method is:
```python
"(" + area_code + ")" + middle_part + "-" + last_part
```

I don't use this method because for me it's hard to visualize where the variable goes in.

## Conditionals
These are the flow charts of code
![flowchart](http://res.cloudinary.com/dkibchpur/image/upload/v1530036656/Screen_Shot_2018-06-26_at_2.02.32_PM.png)

## If
If the conditions are met do something

```python
raining = 'yes'

if raining == 'yes':
    print("Better bring an umbrella")
```

## Elif
Another option. I like to think of this an multiple choice option.

```python
elif raining == 'maybe':
    print("Better bring one so I'm prepared if it rains")
```

## Else
If none of the conditions meet than do this
```python
else:
    print("I don't need to pack an umbrella")
```
