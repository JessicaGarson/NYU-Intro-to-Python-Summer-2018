# PIP!
One of the best known advantages of using Python is for it's robust community, pip is the tool that's most commonly used to download packages from Python.

## So how do I do this?
In the command line type the following but replace package with the name of the package you want to use:

```bash
pip install package
```

## But wait I saw another way to install packages?
If you are using the Anaconda distribution of Python you might have seen another way to install packages. We are starting with pip because it's the most common.

## So let's install some packages
Let's start out by installing [this package to make json easier to work with](https://pypi.org/project/simplejson/).

```bash
pip install simplejson
```

## Let's check to see if this worked

```bash
python
```

```python
import simplejson
```

## Oh no, I got an error
For macs you might need to use this syntax:

```bash
pip3 install simplejson
```

If you had to do this you might want to consider adding an alias to your bash profile.

To set up an alias so all you have to do is type the word `pip`:

```bash
nano ~/.bash_profile
```

And type the following into the editor:

```bash
alias pip='pip3'
```
If you got an error about not having pip installed

I got an error about not having pip installed:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
