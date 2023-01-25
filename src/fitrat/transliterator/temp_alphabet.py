latin_uppercase = [
    "’",
    "‘",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
latin_lowercase = [
    "’",
    "‘",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

lower_vowels = ["а", "е", "и", "о", "у", "ў", "я", "э", "ё", "ю"]
lower_consonants = [
    "б",
    "д",
    "ф",
    "г",
    "ҳ",
    "ж",
    "к",
    "л",
    "м",
    "н",
    "п",
    "қ",
    "р",
    "с",
    "т",
    "в",
    "х",
    "й",
    "з",
    "ғ",
    "ш",
    "ч",
    "ь",
    "ъ",
]

upper_vowels = ["А", "Е", "И", "О", "У", "Ў", "Я", "Э", "Ё", "Ю"]
upper_consonants = [
    "Б",
    "Д",
    "Ф",
    "Г",
    "Ҳ",
    "Ж",
    "К",
    "Л",
    "М",
    "Н",
    "П",
    "Қ",
    "Р",
    "С",
    "Т",
    "В",
    "Х",
    "Й",
    "З",
    "Ғ",
    "Ш",
    "Ч",
    "Ь",
    "Ъ",
]

vowels = lower_vowels + upper_vowels
consonants = lower_consonants + upper_consonants

cyrillic_uppercase = upper_vowels + upper_consonants
cyrillic_lowercase = lower_vowels + lower_consonants

# White space
white_space = [
    " ",
    "\u0009",
    "\u000a",
    "\u000d",
    "\u00a0",
    "\u1680",
    "\u2000",
    "\u2001",
    "\u2002",
    "\u2003",
    "\u2004",
    "\u2005",
    "\u2006",
    "\u2007",
    "\u2008",
    "\u2009",
    "\u200a",
    "\u2028",
    "\u2029",
    "\u202f",
    "\u205f",
    "\u3000",
]

# Punctuation that ends sentences
sentence_boundary = ["...", ".", "?", "!", "…"]

# Left punctuation
left_punctuation = ["(", "[", "{", "“", "‘", "‹", "«", "'", '%"', "''"]

# Right punctuation - excluding the characters that can be used as apostrophe
right_punctuation = sentence_boundary + [
    ",",
    ";",
    ":",
    ")",
    "]",
    "{",
    "”",
    "›",
    "»",
    '%"',
    "''",
]

# Symbols
symbols = ["-", "+", "<", ">", "*", "/"]

# Punctuation
punctuation = right_punctuation + left_punctuation + symbols
