import json
import os

cwd = os.path.dirname(os.path.abspath(__file__))

mapping_lower = {
    "o‘": "ў",
    "g‘": "ғ",
    "yo‘": "йў",
    "sh": "ш",
    "ch": "ч",
    "ya": "я",
    "yu": "ю",
    "yo": "ё",
    "ye": "е",
    "a": "а",
    "b": "б",
    "d": "д",
    "e": "е",
    "f": "ф",
    "g": "г",
    "h": "ҳ",
    "i": "и",
    "j": "ж",
    "k": "к",
    "l": "л",
    "m": "м",
    "n": "н",
    "o": "о",
    "p": "п",
    "q": "қ",
    "r": "р",
    "s": "с",
    "t": "т",
    "u": "у",
    "v": "в",
    "x": "х",
    "z": "з",
    "y": "й",
    "’": "ъ"
}

mapping_upper = {
    "O‘": "Ў",
    "G‘": "Ғ",
    "Sh": "Ш",
    "Ch": "Ч",
    "Ya": "Я",
    "Yu": "Ю",
    "Yo": "Ё",
    "Yo‘": "Йў",
    "E": "Э",
    "A": "А",
    "B": "Б",
    "D": "Д",
    "E": "Е",
    "F": "Ф",
    "G": "Г",
    "H": "Ҳ",
    "I": "И",
    "J": "Ж",
    "K": "К",
    "L": "Л",
    "M": "М",
    "N": "Н",
    "O": "О",
    "P": "П",
    "Q": "Қ",
    "R": "Р",
    "S": "С",
    "T": "Т",
    "U": "У",
    "V": "В",
    "X": "Х",
    "Y": "Й",
    "Z": "З",
    # "’": "Ъ"
}

# with open(cwd + "/exceptions.json") as f:
#     exceptions = json.load(f)
    # exceptions = dict(sorted(exceptions.items(), reverse=True))

vowels_lower = ["a", "e", "i", "o", "u", "o‘", "ya", "ye", "yo", "yu", "yo‘"]
consonants_lower = ["b", "d", "f", "g", "h", "j", "k", "l", "m",
                    "n", "p", "q", "r", "s", "t", "v", "x", "y", "z", "g‘", "sh", "ch"]

vowels_upper = ["A", "E", "I", "O", "U", "O‘", "Ya", "Ye", "Yo", "Yu", "Yo‘"]
consonants_upper = ["B", "D", "F", "G", "H", "J", "K", "L", "M",
                    "N", "P", "Q", "R", "S", "T", "V", "X", "Y", "Z", "G‘", "Sh", "Ch"]

vowels = vowels_lower + vowels_upper
consonants = consonants_lower + consonants_upper

latin_uppercase = vowels_upper + consonants_upper
latin_lowercase = vowels_lower + consonants_lower

cyrillic_uppercase = [
    "А",
    "Б",
    "В",
    "Г",
    "Ғ",
    "Д",
    "Е",
    "Ё",
    "Ж",
    "З",
    "И",
    "Й",
    "К",
    "Қ",
    "Л",
    "М",
    "Н",
    "О",
    "П",
    "Р",
    "С",
    "Т",
    "У",
    "Ў",
    "Ф",
    "Х",
    "Ҳ",
    "Ч",
    "Ш",
    "Ъ",
    "Ь",
    "Э",
    "Ю",
    "Я",
]
cyrillic_lowercase = [
    "а",
    "б",
    "в",
    "г",
    "ғ",
    "д",
    "е",
    "ё",
    "ж",
    "з",
    "и",
    "й",
    "к",
    "қ",
    "л",
    "м",
    "н",
    "о",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ў",
    "ф",
    "х",
    "ҳ",
    "ч",
    "ш",
    "ъ",
    "ь",
    "э",
    "ю",
    "я",
]

latin = latin_lowercase + latin_uppercase
cyrillic = cyrillic_lowercase + cyrillic_uppercase