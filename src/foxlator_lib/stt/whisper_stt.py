
from typing import Dict
import whisper  # type: ignore
import moviepy.editor as mp  # type: ignore
from foxlator_lib.audio import AudioPath
from foxlator_lib.video import Video
import torch


class WhisperSTT():

    def __init__(self, language: str = "en", model: str = 'medium') -> None:
        self.model = self._prepare_model(model)
        self.language = language

    def _prepare_model(self, model: str = 'medium'):
        available_models = whisper.available_models()
        if model not in available_models:
            raise Exception(
                f'Not supported model. Models available: {available_models}')
        return whisper.load_model(model)

    def audio_to_text(self, audio: AudioPath) -> str:
        result: Dict[str, str] = self.model.transcribe(  # type: ignore
            audio=audio.to_wave_soundarray(16000, 2, 1, True),
            task=None,
            language=self.language,
            fp16=torch.cuda.is_available(),
        )  # type: ignore
        print(str(result['text']))
        return str(result['text'])


v = Video("/home/hazka/projects/foxlator-lib/.vscode/video.mp4")
WhisperSTT(language='pl', model='large').audio_to_text(
    audio=v.get_audio_path())
