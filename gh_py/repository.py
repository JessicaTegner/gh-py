class Repository:
    def __init__(self, owner, name, url) -> None:
        self.owner = owner
        self.name = name
        self.url = url
    
    def __str__(self) -> str:
        return f'Repository: {self.owner}/{self.name} ({self.url})'
    
    def __repr__(self) -> str:
        return f'Repository({self.owner!r}, {self.name!r}) {self.url!r}'
    
    def __eq__(self, o: object) -> bool:
        return isinstance(o, Repository) and o.owner == self.owner and o.name == self.name and o.url == self.url
    