# from fitrat.transliterators.lat_cyr.model_compile import model_compile
from hfstol import HFSTOL
import os 

cwd = os.path.dirname(os.path.abspath(__file__))

class LatCyrTransliterator():
	_model = HFSTOL.from_file(cwd + '/model/lat_cyr.hfstol')
	_exception = HFSTOL.from_file(cwd + '/model/exception_pruned.hfstol')

	def _convert_token(self, token: str):
		exc_lookup = self._exception.feed(token)
		if exc_lookup:
			return exc_lookup[0][0]
		else:
			return self._model.feed(token)[0][0]