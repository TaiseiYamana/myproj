#!/bin/sh -ex
target_branch="ghp-deploy"
git branch $target_branch
git config --global user.name "CircleCI deployer"
git config --global user.email "<>"
git checkout $target_branch
git reset --hard origin/master

gcc -o a.out a.c
echo "output of a.out: $(./a.out)" > a.txt

git add a.out a.txt
git commit -m "[skip ci] updates GitHub Pages"
if [ $? -ne 0 ]; then
  echo "nothing to commit"
  exit 0
fi

git remote set-url origin "https://github.com/TaiseiYamana/myproj.git"
git push -f origin $target_branch
