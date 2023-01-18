from enum import Enum
from .cyr_lat.model_compile import model_compile as cyrlat_model
from .lat_cyr.model_compile import model_compile as latcyr_model


class Type(Enum):
	CYRLAT = 0
	LATCYR = 1


class Transliterator:
	__models = {
		Type.CYRLAT: cyrlat_model(),
		Type.LATCYR: latcyr_model()
	}

	def __init__(self, type: Type = Type.CYRLAT) -> None:
		self.model = self.__models[type]

	def convert(self, text: str) -> str:
		return self.model.lookup(text)[0][0]


if __name__=="__main__":
	l = Transliterator()
	print(l.convert("Ерга нима дейсиз? \nШУНГА жуда куп одамлар"))
	print(l.convert("ЕРГА НИМА ДЕЙСИЗ?"))
	print(l.convert("""«Аҳолимиз табиий газ ва электр таъминоти, коммунал хизматлари сифатидан жиддий эътирозларини билдиряпти. Буни барчамиз кўриб турибмиз.
Айниқса, Тошкент шаҳрининг барча даражадаги раҳбарларининг бугунги ҳолатга тайёр эмаслигини мен ўзим ҳам кўриб турибман, халқимиз ҳам кўриб турибди.
Ҳозирги кунда пойтахтда кунлик 3 млн киловатт чеклов ўрнатилгани, 6 мингга яқин улгуржи истеъмолчилар газ тармоғидан узилганига қарамай, 120 та маҳаллада электр ва газ таъминотида узилишлар бўлди. 584 та маҳалладан 120 тасида мана шундай муаммолар бўлди."""))
	print(l.convert("Ш."))
	print(l.convert("Е."))