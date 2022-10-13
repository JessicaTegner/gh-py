import gh_py
from gh_py.repository import Repository

def test_current_repository_type():
    repo = gh_py.current_repository()
    assert isinstance(repo, Repository)
    assert hasattr(repo, "name")
    assert hasattr(repo, "owner")
    assert hasattr(repo, "url")
