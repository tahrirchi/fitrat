from .word_tokenize import UzWordTokenizer

_uz_word_tokenizer = UzWordTokenizer()


def word_tokenize(text: str) -> list[str]:
    """Return a tokenized copy of *text*.

    :param text: text to split into words
    :type text: str
    """
    return _uz_word_tokenizer.tokenize(text)
