# Virtual Environments, PIP and Notebooks
Before we get too deep into data science concepts we have some tooling to cover.

## What is a virtual environment?
We all have different computers and some of those computers carry some baggage. Virtual environments allow us to start fresh which is pretty helpful if we are starting a new project working with teams.

## Let's play around with pip
Let's play around with this environment and install some packages.
```
pip install jupyter
pip install ipython
pip install numpy
pip install pandas
pip freeze
pip freeze > requirements.txt
```

If you wanted to install a pre-made requirements.txt you do the following:
```
pip install -r requirements.txt
```

## pipenv
Pipenv is the latest recommended way to manage packages and dependancies. It creates a virtual environment. This creates a lockfile that allows us to create environments that can be easily updated as packages change. What's also great about this is it provides more windows support than older package management.

[The documentation is pretty good](https://docs.pipenv.org/)

To install type this into the command line.
```
pip install --user pipenv
```

## Anaconda might be a good choice if you want to do a lot of data science type work.
Anaconda is a distribution of Python that has a lot of built in support for data science libraries. It also comes with it's own package manager conda that acts like pipenv or other virtual environments.

[You can download this here](https://www.anaconda.com/download/).

## ipython
Let's check it out. And play around in it.
```
ipython
````

## Jupyter
Jupyter takes the concept to the next level by allowing an environment where you can play around in this interactive environment.
```
jupyter notebook
```

## datetime example
```
import datetime

time = datetime.datetime.now()

def greeting(time):
  name = 'Jess'
  print('Hello {}, the time is {}'.format(name, time))

greeting(time=time)
```

## We can add jupyter notebooks to GitHub and view them there
Let's add this notebook to our GitHub repository.

```python
git add .
git commit -m "adding notebooks to GitHub"
git push
```

## So what do we need for Data Science in Python
Typically we need to clean up data we typically use the library Pandas and numpy, than we need to visualize our data and the libraries that are used are matplotlib, seaborn, bokeh, and plot.ly. For modeling data we typically use scikit learn for such.
