# from fitrat.transliterators.cyr_lat.model_compile import model_compile
import os 
from hfstol import HFSTOL

cwd = os.path.dirname(os.path.abspath(__file__))

class CyrLatTransliterator():
	# _model = model_compile()
	_model = HFSTOL.from_file(cwd + '/model/cyr_lat.hfstol')

	def _convert_token(self, token: str):
		return self._model.feed(token)[0][0]