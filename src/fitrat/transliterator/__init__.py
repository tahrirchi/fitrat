from enum import Enum
from .cyr_lat.model import compile_model as cyrlat_model
from .lat_cyr.model import compile_model as latcyr_model


class Type(Enum):
    LAT = 0
    CYR = 1


class Transliterator:
    __models = {
        Type.LAT: cyrlat_model(), 
        Type.CYR: latcyr_model()
    }

    def __init__(self, *, to: Type = Type.LAT) -> None:
        self.model = self.__models[to]

    def convert(self, text: str) -> str:
        res = self.model.lookup(text)
        if not res:
            return ""
        print(res)
        return res[0][0]
