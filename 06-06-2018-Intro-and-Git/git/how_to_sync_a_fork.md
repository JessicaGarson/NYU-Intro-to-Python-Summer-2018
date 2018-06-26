# How to Sync a Fork
We won't be covering this today, but it's commonly asked question.

Use this code to stay current when the contents of the repository have changed.

```
git clone https://github.com/yourname/name_of_repo.git
cd sample_to_be_forked
git remote add upstream https://github.com/repo_creator/name_of_repo.git
git fetch upstream
git checkout master
git merge upstream/master
git push
```
