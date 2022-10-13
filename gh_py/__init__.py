import json

from .internal import gh
from .repository import Repository

def current_repository() -> Repository:
    info = gh.exec('repo view --json owner,name,url')
    info = json.loads(info)
    r = Repository(owner=info["owner"]['login'], name=info['name'], url=info['url'])
    return r
