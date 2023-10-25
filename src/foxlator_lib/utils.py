
def get_version() -> str:
    import importlib.metadata
    return importlib.metadata.version('foxlator_lib')


class FileSystem(object):
    def is_file(self) -> bool:
        pass
