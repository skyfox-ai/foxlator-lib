from typing import Any
from utils import base
import numpy as np
from numpy.typing import NDArray
from moviepy.editor import AudioFileClip  # type: ignore
import tempfile
import os
from scipy.io.wavfile import write  # type: ignore
from foxlator_lib.audio import AudioPath


class TestAudioPath(base.TestBase):

    def setUp(self):
        self.audio_rate = 44100
        self.stereo_audio_array = np.random.uniform(
            -1, 1, (self.audio_rate*2, 2))
        self.stereo_audio_path = AudioPath(
            self.create_test_audio(self.stereo_audio_array))

    def create_test_audio(self, audio_array: NDArray[Any]):
        with tempfile.NamedTemporaryFile() as tmp:
            write(tmp.name, self.audio_rate, audio_array)
            return AudioFileClip(tmp.name)

    def test_save_success(self):
        with tempfile.NamedTemporaryFile() as tmp:
            self.stereo_audio_path.save(tmp.name)
            self.assertTrue(os.path.exists(tmp.name + ".mp3"))

    def test_to_soundarray_stereo_audio(self):
        to_soundarray_value = self.stereo_audio_path.to_soundarray()
        self.assertEqual(to_soundarray_value.shape,
                         self.stereo_audio_array.shape)
        np.testing.assert_allclose(
            to_soundarray_value, self.stereo_audio_array, rtol=1e-3, atol=1e-3)

    def test_to_wave_soundarray_smoke(self):
        try:
            result = self.stereo_audio_path.to_wave_soundarray()
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")
        self.assertIsNotNone(result, "Result should not be None")
        self.assertTrue(result.ndim == 1)
