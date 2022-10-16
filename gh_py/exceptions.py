class GhPyException(Exception):
    """Base class for all exceptions in gh_py."""
    pass

class GhPyGhException(GhPyException):
    """Base class for all exceptions in gh_py that are caused by gh."""
    pass

class GhPyNotARepositoryException(GhPyException):
    """Exception raised when the current directory is not a git repository."""
    pass
