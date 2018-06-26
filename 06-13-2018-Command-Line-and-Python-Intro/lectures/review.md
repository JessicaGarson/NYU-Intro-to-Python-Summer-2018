# Review
## What is programming?
Programming is creating a set of directions for your computer to follow.
## Who is a developer?
Anyone who commits code to a code to a codebase (all of us now!).
## What open source code?
Code that is available in the public domain (we also all open source developers).
## What is git?
Git is a version control software that allows us to collaborate with teams. We can use git to go back in time, and also keep track of every commit we ever create.
## What is a repository?
A receptacle where things are or may be stored.
## What is a fork?
A fork allows us to to create our version of a repository so that we can make our own changes to it.
## What happens when we clone a repository?
When we clone a repository we bring our repository into our local environment as a folder and therefore we can make changes into it.
## What is a pull request?
A pull request is how we ask to bring changes back into the repository?
## What is markdown used for?
Markdown helps us as developers communicate with each other by creating a place for us to explain our code. If you checked the `initialize repository with README file` that creates a markdown file for you to explain your repository.
## Let's commit a file and make a pull request from GitHub's workflow
We'll be working with this repository:
https://github.com/yinakhoilian/pair-programming-June-6th
## Let's make commit a file and make a pull request from the command line.
I've gone ahead and forked Lauren's repo.
Let's visit my fork located on https://github.com/JessicaGarson/pair-programming-June-6th. From there we can grab the HTTPs to clone this repository.
```bash
git clone https://github.com/JessicaGarson/pair-programming-June-6th.git
```
Let's change directories into our new repository:
```bash
cd pair-programming-June-6th
```
Since I have the shell commands installed I can open this open in atom from the command line. Or I can find the directory just as I would by using the finder interface.
```bash
atom .
```
From here I can create a new file from atom called `demo.md` and edit it to look something like this:
```markdown
## Class demo - command line mac
We are going to add this back in as a pull request.
```
After we save our file, we can go add this back into our repository.
```bash
git add demo.md
git status
git commit -m "adding new markdown file"
git status
git push
```
Now let's check our clone and see if the file is still there. If so from the GitHub site we can submit a pull request to ask to put this file back in Lauren's repository.

## Class demo command line PC
We'll do the same process but on a PC. We will use this [repo](https://github.com/JessicaGarson/for_class_command_line_demo_PC).
