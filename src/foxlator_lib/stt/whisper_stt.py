
import torch
from typing import Dict
import whisper  # type: ignore
import moviepy.editor as mp  # type: ignore
from foxlator_lib.audio import AudioPath


class WhisperSTT():

    def __init__(self, language: str = "en", model: str = 'medium') -> None:
        self.model = self._prepare_model(model)
        self.language = self._get_whisper_language(language)

    def _prepare_model(self, model: str = 'medium'):
        available_models = whisper.available_models()
        if model not in available_models:
            raise Exception(
                f'Not supported model. Models available: {available_models}')
        return whisper.load_model(model)

    def _get_whisper_language(self, language: str):
        all_langs: Dict[str, str] = whisper.tokenizer.LANGUAGES  # type: ignore
        if not isinstance(all_langs, Dict):
            raise Exception("Language dict does not exist")
        if language in all_langs.keys():
            return all_langs[language]
        if language in all_langs.values():
            return language
        raise Exception(
            f'Not supported languages. Models available: {all_langs}')

    def audio_to_text(self, audio: AudioPath) -> str:
        result: Dict[str, str] = self.model.transcribe(  # type: ignore
            audio=audio.to_wave_soundarray(16000, 2, 1, True),
            task=None,
            language=self.language,
            fp16=torch.cuda.is_available(),
        )  # type: ignore
        return str(result['text'])
