# CSCI040: Continuous Integration Example

<img src="https://github.com/yyuan29/yyuan29python.github.io/workflows/tests/badge.svg" />

This repo is for an in-class example of how to use doctests and continuous integration on github.

**STEP 1:**
Transfer files from github to your laptop.

```
$ git clone https://github.com/mikeizbicki/example-doctests
```

Verify it worked:
```
$ pwd
/home/user/proj
$ cd example-doctests
$ pwd
/home/user/proj/example-doctests
$ ls
README.md example.py
```

**STEP 2:**
Get the doctests to pass.

You can run the doctests in your terminal with the command
```
$ python3 -m doctest example.py
```

The command above shows only failing doctests.
Adding the `--verbose` flag will show both passing and failing doctests.
```
$ python3 -m doctest --verbose example.py
```

**STEP 3:**
Put your updated code on github.

Uploading to github always has two steps:

1. "Committing" your changes to the local repo.
    ```
    $ git add example.py
    $ git commit -m 'update example.py'
    ```

2. "Pushing" your changes to the remote repo (i.e. github).
    ```
    $ git push origin master
    ```

    The command above should fail for you, because it is trying to push the changes to *my* account and you do not have permission for that.
    Instead, you must tell git to push the changes to your account:

    1. Create your own empty repository via the github interface.
    2. Use the following commands to tell git to use your new repo url instead of mine.
        ```
        $ git remote rm origin
        $ git remote add origin <your_url>
        ```
    3. Re-run the git push command.

**STEP 4:**
Notice that the red test cases badge claims that your test cases are failing even if they are passing.

To fix this, you must:
1. enable github actions through the web interface
1. modify the `README.md` file so that the image points to your repository instead of mine
1. Rerun the add/commit/push commands to upload your changes to github
