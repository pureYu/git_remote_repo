"""
CLI tool for cloning given git repository
and executing the containing python file with a number parameter x,
prints the result (e.g. x^2) and cleans up the working directory.

This script takes 3 parameters:
    * str - location of the remote git repository
    * str - git commit reference that should be executed and
    * int - the number x that should be passed to the downloaded script.

Usage example:
    python clone_execute.py remote_git_repository_path git_commit_reference x_param_to_pass
    python clone_execute.py https://github.com/pureYu/git_remote_repo_toclone 427b979ce8d49ae7e639197c3b5c1fad0415d5c4 12

"""
import argparse
import os
import shutil
from git import Repo
import subprocess



DIR_FOR_CLONED_REPO = 'cloned_repository'


def remove_target_dir(path):
    """ Recursively delete a directory tree """
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
        except:
            print('Error while deleting directory')


def print_remote_scripit_results(script_path, script_param):
    """ Prints the result (e.g. x^2) of downloaded script execution
        should be refactored - script name hardcoded
    """
    print('----------------------')
    print('Downloaded script printed:\n')
    sys_command = "python {}/script.py {}".format(script_path, script_param)
    output = subprocess.check_output(sys_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    print(output.strip())
    print('----------------------')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('git_repo_to_clone')
    parser.add_argument('git_commit_hash')
    parser.add_argument('x', type=int)
    args = parser.parse_args()

    git_repo_to_clone = args.git_repo_to_clone
    git_commit_hash = args.git_commit_hash
    param_to_pass = args.x

    # url parsing should be added here
    # hash check/parsing should be added here

    print('----------------------')
    repo_path = os.path.join(os.getcwd(), DIR_FOR_CLONED_REPO)
    remove_target_dir(repo_path)
    repo = None


    try:
        # Repo object used to programmatically interact with Git repositories
        repo = Repo.clone_from(git_repo_to_clone, repo_path)
        # check that the repository loaded correctly
        if not repo.bare:
            print('Repo at {} successfully loaded.'.format(repo_path))
            print('Hashes:')
            commits = list(repo.iter_commits('master'))
            hash_list = []
            for commit in commits:
                # unique SHA key
                print(commit.hexsha)
                hash_list.append(commit.hexsha)
    except Exception as e:
        print('Exception: Could not load repository at {} \n{}'.format(repo_path, e))
        return


    if repo is not None:
        try:
            repo.git.checkout(git_commit_hash)
        except Exception as e:
            print('\nException: can\'t checkout to commit with hash \"{}\" \n {}'.format(git_commit_hash, e))
            return

    print_remote_scripit_results(repo_path, param_to_pass)
    remove_target_dir(repo_path)
    print("Good news! Process finished, evidence destroyed.")



if __name__ == '__main__':
    main()
