# fitrat
NLP library for Uzbek. It includes morphological analysis, transliterators, language identifiers, tokenizers and many more. 

It is named after historian and linguist Abdurauf Fitrat, who was one of the creators of Modern Uzbek, as well as the first Uzbek professor. 

## Transliterator

### Cyrillic-Latin transliterator

Example of usage:

```python
from fitrat import CyrLatTransliterator

sentence = CyrLatTransliterator("Кеча циркка бордим")

print(sentence)
```
