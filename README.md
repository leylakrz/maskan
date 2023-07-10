# Maskan Bank Code Challenge

## Postman Collection

https://api.postman.com/collections/27176461-69809133-e154-4cfc-bacf-51b54d870053?access_key=PMAT-01H4ZG69JTXJ9AAHG5MBK70M02

## Git Workflow

We use Git for version control in our project. Our workflow consists of the following branches:

- **dev**: The development branch. This is where new features and bug fixes are merged first. All feature, debug, and hotfix
  branches should be merged into this branch.
- **stage**: The staging branch. This branch is used for testing changes before they are deployed to production. Only dev,
  main, and hfix branches should be merged into this branch.
- **main**: The production branch. This is the branch that represents the current state of the project in production. Only
  stage and hfix branches should be merged into this branch.

### Creating a new branch

When working on a new feature, bug fix, or hotfix, create a new branch based on the dev branch:

```
git checkout dev
git checkout -b feat/feature-name   # for a new feature branch
git checkout -b fix/bug-fix-name   # for a new bug fix branch
git checkout -b hfix/hotfix-name   # for a new hotfix branch
```

### Merging changes

To merge changes into the dev branch, first ensure that your branch is up to date with the latest changes from dev:

```
git checkout dev
git pull
git checkout feat/feature-name   # or fix/bug-fix-name, or hfix/hotfix-name
git merge dev
```

To merge changes into the stage branch, first ensure that your branch is up to date with the latest changes from both
dev and main:

```
git checkout dev
git pull
git checkout main
git pull
git checkout stage
git merge dev
git merge main
```

To merge changes into the main branch, first ensure that your branch is up to date with the latest changes from both
dev, stage, and main:

```
git checkout dev
git pull
git checkout main
git pull
git checkout stage
git pull
git checkout main
git merge stage
```