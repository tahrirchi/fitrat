from pathlib import Path

from hfstol import HFSTOL

_MODEL_PATH = str(Path(__file__).parent / "model" / "cyr_lat.hfstol")


class CyrLatTransliterator:
    _model = HFSTOL.from_file(_MODEL_PATH)

    def _convert_token(self, token: str):
        return self._model.feed(token)[0][0]
