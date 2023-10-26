
from .file_system import FileSystem
from ..error import BaseError


def get_version() -> str:
    import importlib.metadata
    return importlib.metadata.version('foxlator_lib')
