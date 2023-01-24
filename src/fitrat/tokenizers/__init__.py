from .word_tokenize import UzWordTokenizer

_uz_word_tokenizer = UzWordTokenizer()

def word_tokenize(text, language="english", preserve_line=False):
	"""
	Return a tokenized copy of *text*,
	using NLTK's recommended word tokenizer
	(currently an improved :class:`.TreebankWordTokenizer`
	along with :class:`.PunktSentenceTokenizer`
	for the specified language).

	:param text: text to split into words
	:type text: str
	:param language: the model name in the Punkt corpus
	:type language: str
	:param preserve_line: A flag to decide whether to sentence tokenize the text or not.
	:type preserve_line: bool
	"""
	return _uz_word_tokenizer.tokenize(text)
	# sentences = [text] if preserve_line else sent_tokenize(text, language)
	# return [
	#     token for sent in sentences for token in _treebank_word_tokenizer.tokenize(sent)
	# ]