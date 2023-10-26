
from .audio import AudioPath
from .utils import FileSystem
from .error import BaseError


class VideoError(BaseError):
    pass


class Video(object):
    def __init__(self, path: str, fs=FileSystem()):
        self.path = path
        self.fs = fs

        if (not self.fs.is_file(path)):
            raise VideoError()

    def get_audio_path(self) -> AudioPath:
        return AudioPath()
