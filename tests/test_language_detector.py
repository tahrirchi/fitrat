from fitrat import LanguageDetector


class TestLanguageDetector:
    def setup_method(self):
        self.ld = LanguageDetector()

    def test_uzbek_latin(self):
        assert self.ld.is_uzbek("bu o'zbekchada yozilgan matn") is True

    def test_uzbek_cyrillic(self):
        assert self.ld.is_uzbek("бу узбекча матн") is True

    def test_russian_not_uzbek(self):
        assert self.ld.is_uzbek("Текст на русском языке") is False

    def test_is_latin(self):
        assert self.ld.is_latin("bu o'zbekchada yozilgan matn") is True

    def test_is_cyrillic(self):
        assert self.ld.is_cyrillic("бу узбекча матн") is True

    def test_predict_returns_label(self):
        label = self.ld.predict("hello world")
        assert isinstance(label, tuple)
        assert label[0].startswith("__label__")
