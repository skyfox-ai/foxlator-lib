
from ddt import ddt, data  # type: ignore

from utils import base
from src import foxlator_lib as fll


@ddt
class VideoTests(base.TestBase):
    fs = base.FileSystemMock()
    invalid_paths = ['path-without-extension',
                     'path.mp3', 'path.jpg', 'relative/path/file.obj']

    def test_when_creating_video_from_not_existing_path_should_throw_error(self):
        self.fs.push_is_file_return(False)
        self.assertRaises(fll.video.VideoError,
                          lambda: fll.video.Video('some-path.mp4', self.fs))

    @data(*invalid_paths)
    def test_when_creating_video_from_path_with_not_supported_extensions_should_throw_error(self, path: str):
        self.fs.push_is_file_return(True)
        self.assertRaises(fll.video.VideoError,
                          lambda: fll.video.Video(path, self.fs))
