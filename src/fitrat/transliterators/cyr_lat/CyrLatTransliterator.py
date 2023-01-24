from fitrat.transliterators.cyr_lat.model_compile import model_compile

class CyrLatTransliterator():
	_model = model_compile()

	def _convert_token(self, token: str):
		return self._model.lookup(token)[0][0]