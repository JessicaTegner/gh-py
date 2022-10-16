import json

from .internal import gh
from .repository import Repository
from.exceptions import GhPyGhException, GhPyNotARepositoryException

def current_repository() -> Repository or GhPyNotARepositoryException:
    """Get the current git repository as a Repository object.

    Raises:
        GhPyNotARepositoryException: If the current directory is not a git repository.

    Returns:
        Repository: The current git repository.
    """    
    try:
        info = gh.exec('repo view --json owner,name,url')
        info = json.loads(info)
        r   = Repository(owner=info["owner"]['login'], name=info['name'], url=info['url'])
        return r
    except GhPyGhException:
        raise GhPyNotARepositoryException("The current directory is not a git repository.")
