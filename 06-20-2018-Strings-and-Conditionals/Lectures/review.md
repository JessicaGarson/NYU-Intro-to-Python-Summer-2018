# Review

## Command Line
I'll type these commands and we'll yell at what they do.

```bash
pwd
cd Documents
ls
mkdir review
cd ..
cd Documents/review
```

For macs:
```bash
touch hello_world.py
```

For PCs:
```bash
New-Item hello_world.py
```

```bash
ls
```

## When does atom . work
Atom . only works when atom is open on your machine. Opening via `open` in atom is alright. We'll demo both methods.

## Let's create a hello world file
Inside of Atom let's type the following in.

```python
print('Hello World!')
```

And inside of our terminal we can run this file by typing the following:

```bash
python hello_world.py
```

```bash
cat hello_world.py
more hello_world.py
mv hello_world.py hello.py
```

We will need to create a repository for ourselves and clone that repository into our local environment.

```bash
cd ~
mv hello.py mv NYU-Intro-to-Python-Your-Name/hello.py
```

We can get this back into GitHub with the following syntax:

```bash
git add hello.py
git commit -m "adding to portfolio"
git push
```

## How to Save Terminal Output
To save your command line session to a file use the following syntax.

```bash
history > command_line_output.txt
```

## Git Configuration
Some folks mentioned they are having issues with git configuration.

```bash
git config --global user.name UserName
git config --global user.email your.email@provider.com
```

## A Note on 2 Factor Authentication
If you are using 2 factor authentication for GitHub (which you should be). If you are using HTTPS Git, instead of entering your password, enter a personal access token. These can be created by going to your
[personal access tokens page](https://github.com/settings/tokens).

## Questions
Please feel free to ask any questions you might have.
