# Fitrat

NLP library for Uzbek. It includes morphological analysis, transliterators, language identifiers, tokenizers and many more.

It is named after historian and linguist Abdurauf Fitrat, who was one of the creators of Modern Uzbek, as well as the first Uzbek professor.

# Installation

```
pip install fitrat
```

# Usage

```python
from fitrat import Transliterator, Type

t = Transliterator()
result = t.convert("Кеча циркка бордим")
print(result)

t2 = Transliterator(Type.LATCYR)
result = t2.convert("Men Tursunxonman, sog' bo'lasiz!")
print(result)
```
