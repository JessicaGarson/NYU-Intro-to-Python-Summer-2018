# So What is Python Anyways?
As we briefly discussed last week Python is basically the Swiss army knife of programming languages, you can make websites with it, you can preform automation tasks, you can use Python for system administration tasks, make games with it and use it for data science.

## Python has been around since the 80s
It was named after Monty Python and has been gaining in popularity due to it's readability, and robust community around the language. It was created by a man named Guido van Rossum. There are libraries for just about anything you can imagine in Python.

## Awkwardness over Python 2 vs Python 3
In the community there was some split for a bit over Python 2 verses Python 3 due backwards compatablity of the languge. At this point Python 3 is becomming the standard here. For this purpose we will be soley writing code in Python 3. 

## Philosophy of the language
```python
import this
```

## I heard people say everything is an object in Python - What does this mean?
From [StackOverflow](https://stackoverflow.com/questions/865911/is-everything-an-object-in-python-like-ruby)- 
"Everything in Python is an object, and almost everything has attributes and methods. All functions have a built-in attribute `__doc__`, which returns the doc string defined in the function's source code. The sys module is an object which has (among other things) an attribute called path. And so forth.

Still, this begs the question. What is an object? Different programming languages define “object” in different ways. In some, it means that all objects must have attributes and methods; in others, it means that all objects are subclassable. In Python, the definition is looser; some objects have neither attributes nor methods, and not all objects are subclassable. But everything is an object in the sense that it can be assigned to a variable or passed as an argument to a function."

## Someone last week asked if Python is interpreted or complied?
- Interpreted means means a program is reading the source file a line at a time, and doing what it says.
- Compiled means to convert a program in a high-level language into a binary executable full of machine code so it creates CPU instructions so that your program can run.
- [The answer for Python is it's complicated.](https://nedbatchelder.com/blog/201803/is_python_interpreted_or_compiled_yes.html)
- For Python the source is compiled into a something know bytecode. These are instructions similar in spirit to CPU instructions, but instead of being executed by the CPU, they are executed by software called a virtual machine.

## Resources
- [Why Learn Python?](https://news.codecademy.com/why-learn-python/)
- [What is Python](http://blog.teamtreehouse.com/what-is-python)
- [Drastically Improve Your Python: Understanding Python's Execution Model](https://jeffknupp.com/blog/2013/02/14/drastically-improve-your-python-understanding-pythons-execution-model/)
