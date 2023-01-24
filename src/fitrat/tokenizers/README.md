# Tokenization

Given a character sequence and a defined document unit, tokenization is the task of chopping it up into pieces, called tokens , perhaps at the same time throwing away certain characters, such as punctuation. Here is an example of tokenization [[1]](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html)

## Word tokenization

Uzbek has apostrophed digraphs o‘ and g‘ and apostrophe (tutuq belgisi).

There's no standard for these apostrophes:

- `0x2018` and `0x2019`
- `0x2BB` and `0x2BC`.

Either one is correct.

But, it is wrong to just use the straight apostrophe ', or any other type of apostrophe.

This inconsistency creates a lot of problems, so we have to automatically handle them inside this module, since we don't want to tokenize incorrectly.

Example input:

```python
>>> from fitrat import word_tokenize
>>> word_tokenize("Qo'pol ish ekan!")
["Qo'pol", "ish", "ekan", "!"]
```

With normalizing the apostrophes:

```python
>>> from fitrat import word_tokenize
>>> word_tokenize("Qo'pol ish ekan!", normalize_apostrophes=True)
["Qo‘pol", "ish", "ekan", "!"]
```

## Sentence tokenization

We're using the standard sentence tokenization from `ntlk` library. We haven't found any major peculiarities of sentence tokenization in Uzbek, so we think the generic tokenization can suit well:

```python
>>> from nltk import sent_tokenize
>>> s = '''Piyoz endi 4000 so'm turarkan\nToshkentda. Narx navo oshib ketibdi'''
>>> sent_tokenize(s)
["Piyoz endi 4000 so'm turarkan", 'Narx navo oshib ketibdi']
```
