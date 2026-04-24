from pathlib import Path

from hfstol import HFSTOL

_MODEL_DIR = Path(__file__).parent / "model"


class LatCyrTransliterator:
    _model = HFSTOL.from_file(str(_MODEL_DIR / "lat_cyr.hfstol"))
    _exception = HFSTOL.from_file(str(_MODEL_DIR / "exception_pruned.hfstol"))

    def _convert_token(self, token: str):
        exc_lookup = self._exception.feed(token)
        if exc_lookup:
            return exc_lookup[0][0]
        else:
            return self._model.feed(token)[0][0]
