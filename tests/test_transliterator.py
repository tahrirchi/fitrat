from fitrat import Transliterator, WritingType


class TestCyrToLat:
    def setup_method(self):
        self.t = Transliterator(to=WritingType.LAT)

    def test_basic(self):
        assert self.t.convert("Кеча циркка бордим") == "Kecha sirkka bordim"

    def test_with_punctuation(self):
        assert self.t.convert("Кеча циркка бордим.") == "Kecha sirkka bordim."

    def test_empty_string(self):
        assert self.t.convert("") == ""

    def test_only_punctuation(self):
        assert self.t.convert("...") == "..."

    def test_single_word(self):
        assert self.t.convert("салом") == "salom"

    def test_uppercase(self):
        result = self.t.convert("ТОШКЕНТ")
        assert result == "TOSHKENT"


class TestLatToCyr:
    def setup_method(self):
        self.t = Transliterator(to=WritingType.CYR)

    def test_basic(self):
        assert self.t.convert("Kecha sirkka bordim") == "Кеча циркка бордим"

    def test_with_punctuation(self):
        assert self.t.convert("Kecha sirkka bordim.") == "Кеча циркка бордим."

    def test_empty_string(self):
        assert self.t.convert("") == ""

    def test_only_punctuation(self):
        assert self.t.convert("...") == "..."

    def test_single_word(self):
        assert self.t.convert("salom") == "салом"
