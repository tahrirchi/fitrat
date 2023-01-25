from enum import Enum
from .cyr_lat.CyrLatTransliterator import CyrLatTransliterator
from .lat_cyr.LatCyrTransliterator import LatCyrTransliterator

class WritingType(Enum):
    LAT = 0
    CYR = 1

class Transliterator:
	__models = {
		WritingType.LAT: CyrLatTransliterator(),
		WritingType.CYR: LatCyrTransliterator()
	}

	def __init__(self, to: WritingType = WritingType.LAT) -> None:
		self.model = self.__models[to]

	def convert(self, text: str):
		running_token = ""
		result_text = ""
		for c in text:
			if c.isalpha():
				running_token += c
			else:
				result_text += self.model._convert_token(running_token) + c
				running_token = ""

		result_text += self.model._convert_token(running_token)

		return result_text


# if __name__=="__main__":
# 	l = Transliterator()
# 	print(l.convert("Ерга нима дейсиз? \nШУНГА жуда куп одамлар"))
# 	print(l.convert("ЕРГА НИМА ДЕЙСИЗ?"))
# 	print(l.convert("""«Аҳолимиз табиий газ ва электр таъминоти, коммунал хизматлари сифатидан жиддий эътирозларини билдиряпти. Буни барчамиз кўриб турибмиз.
# Айниқса, Тошкент шаҳрининг барча даражадаги раҳбарларининг бугунги ҳолатга тайёр эмаслигини мен ўзим ҳам кўриб турибман, халқимиз ҳам кўриб турибди.
# Ҳозирги кунда пойтахтда кунлик 3 млн киловатт чеклов ўрнатилгани, 6 мингга яқин улгуржи истеъмолчилар газ тармоғидан узилганига қарамай, 120 та маҳаллада электр ва газ таъминотида узилишлар бўлди. 584 та маҳалладан 120 тасида мана шундай муаммолар бўлди."""))
# 	print(l.convert("Ш."))
# 	print(l.convert("Е."))