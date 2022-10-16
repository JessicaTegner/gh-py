import os

import pytest

import gh_py

def test_exec_success():
    assert gh_py.exec('repo view --json owner,name,url') != ""

def test_exec_failure():
    # get current working dir.
    cwd = os.getcwd()
    # change to a non git repo dir.
    os.chdir("../../")
    # test
    with pytest.raises(gh_py.GhPyGhException):
        gh_py.exec('repo view --json owner,name,url')
    # change back to original dir.
    os.chdir(cwd)
