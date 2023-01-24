import fasttext
import os 

cwd = os.path.dirname(os.path.abspath(__file__))

class LanguageDetector():
	"""
	A wrapper class for the fasttext library's language detection model.
	It detects Uzbek Cyrillic, Uzbek Latin, Russian, English and other languages listed in README.md

	Attributes:
		model (fasttext.FastText._FastText): pre-trained language detection model loaded from 'langdetect.ftz' file.

	"""

	def __init__(self):
		self.model = fasttext.load_model(cwd + '/model/langdetect.ftz')
	

	def predict(self, text: str):
		"""
		Predict the language of the input text.
		
		Args:
			text (str): input text for language prediction.
		
		Returns:
			tuple: containing the predicted language label and probability.
		"""
		label, _ = self.model.predict(text)
		return label

	def is_cyrillic(self, text: str) -> bool:
		"""
		Check if the given text is written in Cyrillic script.
		
		Parameters:
			text (str): The text to be checked.
			
		Returns:
			bool: True if the text is written in Cyrillic script, False otherwise.
		"""
		label = self.predict(text)
		return label[0] == "__label__uz_cyr"


	def is_latin(self, text: str) -> bool:
		"""
		Check if the given text is written in Latin script.
		
		Parameters:
			text (str): The text to be checked.
			
		Returns:
			bool: True if the text is written in Latin script, False otherwise.
		"""
		label = self.predict(text)
		return label[0] == "__label__uz_lat"

	def is_uzbek(self, text: str) -> bool:
		return self.is_latin(text) or self.is_cyrillic(text)

# if __name__=="__main__":
# 	d = LanguageDetector()

# 	print(d.predict("bolaa"))