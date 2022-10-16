import os
import pytest

import gh_py
from gh_py.repository import Repository

def test_current_repository():
    repo = gh_py.current_repository()
    assert repo.name == "gh-py"

def test_current_repository_is_not_a_repository():
    # get the current directory
    cwd = os.getcwd()
    # change to a directory that is not a git repository
    os.chdir("../../")
    # test that the current directory is not a git repository
    with pytest.raises(gh_py.exceptions.GhPyNotARepositoryException):
        gh_py.current_repository()
    # change back to the original directory
    os.chdir(cwd)

def test_current_repository_type():
    repo = gh_py.current_repository()
    assert isinstance(repo, Repository)
    assert hasattr(repo, "name")
    assert hasattr(repo, "owner")
    assert hasattr(repo, "url")
