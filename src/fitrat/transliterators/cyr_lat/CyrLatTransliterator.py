from fitrat.transliterators.cyr_lat.model_compile import model_compile
import os 
from hfst_dev import HfstInputStream

cwd = os.path.dirname(os.path.abspath(__file__))

class CyrLatTransliterator():
	# _model = model_compile()
	_model = HfstInputStream(cwd + '/model/cyr_lat.hfst').read()

	def _convert_token(self, token: str):
		return self._model.lookup(token)[0][0]