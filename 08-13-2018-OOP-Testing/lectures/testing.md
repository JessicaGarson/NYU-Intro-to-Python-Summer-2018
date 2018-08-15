# Test Driven Development

## Why test?
Testing is the best way to figure out if your code works the way you think it does. It also helps you write better more reliable code. It also saves you times because testing is easy but debugging is hard. I like to think of testing as preventative debugging.

## Unit Testing
So let's say we have this code:
```
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return float(a) / b


def main():
    print(add(a=3, b=6))
    print(subtract(a=5, b=2))
    print(multiply(a=3, b=6))
    print(divide(a=5, b=2))


if __name__ == "__main__":
    main()
```

And these would be the tests:
```python
import my_math
import unittest


class TestAdd(unittest.TestCase):
    """
    Test the add function from the my_my_math.py program
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = my_math.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = my_math.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = my_math.add('abc', 'def')
        self.assertEqual(result, 'abc def')


class TestSubtract(unittest.TestCase):
    """
    Test the subtract function from the my_math.py program
    """
    def test_subtract_integers(self):
        result = my_math.subtract(3, 1)
        self.assertEqual(result, 0)

    def test_subtract_floats(self):
        result = my_math.subtract(1.0, 0.5)
        self.assertEqual(result, 0.5)

    def test_subtract_strings(self):
        self.assertRaises(TypeError, my_math.subtract, ("xyz", "z"))

# Add a class for testing the multiply function

# Add a class for testing divide function


if __name__ == '__main__':
    unittest.main()
```

## Why places don't test
It's hard. Testing often requires a culture change in an organization and it requires you to rethink the way you write code.

## Don't look at testing as paperwork that needs to get done.

We know it's something we should do but don't, and it is simply an engineering task that needs to get done.

## But really everyone tests in some way
Usually, the tests that are created aren't good or useable.

## Asserts
- assert: base assert allowing you to write your own assertions
- assertEqual(a, b): check a and b are equal
- assertNotEqual(a, b): check a and b are not equal
- assertIn(a, b): check that a is in the item b
- assertNotIn(a, b): check that a is not in the item b
- assertFalse(a): check that the value of a is False
- assertTrue(a): check the value of a is True
- assertIsInstance(a, TYPE): check that a is of type "TYPE"
- assertRaises(ERROR, a, args): check that when a is called with args that it raises ERROR

## What makes a test good
Good tests are repeatable, fast, informative, reliable, and focused.

## The . addicted
Each test you pass you get a . for and folks who are super into testing often refer to themselves as . addictive.

## Your functions, they do too much
Since you need to test as much as possible your functions will start to do less

## What is test driven development

When you start with testing to create your programs instead of writing code and adjusting. You use the tests to drive your process.
