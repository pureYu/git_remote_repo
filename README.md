# App that clones remote git repo and executes python file with given parameter

Python3 application that
clones a remote git repository into a workspace directory,
executes/evaluates the containing python file with a number parameter x,
prints the result (e.g. x^2) and
cleans up the working directory.

The application should takes parameters:
- location of the remote git repository
- git commit reference that should be executed and
- the number x

Unit tests are not required but api documentation is. There should be a requirements.txt for easy setup and the app should be managed in a git repository for the main application and a git repository for the ‘script’.

Script can be launched from shell:

```
python clone_execute.py <remote_git_repository_path> <git_commit_reference> <x_param_to_pass>
```


e.g.:
```
python clone_execute.py https://github.com/pureYu/git_remote_repo_toclone 427b979ce8d49ae7e639197c3b5c1fad0415d5c4 12
```

