from fitrat.transliterators.lat_cyr.model_compile import model_compile
from hfst_dev import HfstInputStream
import os 

cwd = os.path.dirname(os.path.abspath(__file__))

class LatCyrTransliterator():
	_model = HfstInputStream(cwd + '/model/lat_cyr.hfst').read()
	_exception = HfstInputStream(cwd + '/model/exception_pruned.hfst').read()

	def _convert_token(self, token: str):
		exc_lookup = self._exception.lookup(token)
		if exc_lookup:
			return exc_lookup[0][0]
		else:
			return self._model.lookup(token)[0][0]