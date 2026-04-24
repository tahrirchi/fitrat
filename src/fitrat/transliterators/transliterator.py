from enum import Enum

from .cyr_lat.CyrLatTransliterator import CyrLatTransliterator
from .lat_cyr.LatCyrTransliterator import LatCyrTransliterator


class WritingType(Enum):
    LAT = 0
    CYR = 1


class Transliterator:
    __models = {WritingType.LAT: CyrLatTransliterator(), WritingType.CYR: LatCyrTransliterator()}

    def __init__(self, to: WritingType = WritingType.LAT) -> None:
        self.model = self.__models[to]

    def convert(self, text: str):
        running_token = ""
        result_text = ""
        for c in text:
            if c.isalpha():
                running_token += c
            else:
                if running_token:
                    result_text += self.model._convert_token(running_token)
                result_text += c
                running_token = ""

        if running_token:
            result_text += self.model._convert_token(running_token)

        return result_text
