import unittest
# any utility functions go here


class TestBase(unittest.TestCase):
    pass

#     def create_test_video_file(self):
# frame = np.zeros((480, 640, 3), dtype=np.uint8)
# frame.fill(255)
# video_clip = VideoClip(frame, duration=2)
# with tempfile.NamedTemporaryFile(suffix=".mp4") as temp_file:
#     temp_path = temp_file.name
#     video_clip.write_videofile(temp_path, codec="libx264", fps=25)
#     return temp_path
