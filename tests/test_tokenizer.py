from fitrat import word_tokenize


def test_basic_tokenization():
    result = word_tokenize("Bugun o'zbekchada gapirishga qaror qildim!")
    assert result == ["Bugun", "o'zbekchada", "gapirishga", "qaror", "qildim", "!"]


def test_empty_string():
    assert word_tokenize("") == []


def test_single_word():
    assert word_tokenize("salom") == ["salom"]


def test_punctuation_only():
    result = word_tokenize("...")
    assert result == ["..."]
