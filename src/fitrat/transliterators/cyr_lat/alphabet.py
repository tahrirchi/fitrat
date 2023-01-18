lower_case = {
	"ў ъ" : "o ‘",	# Special rule: мўъжиза ->  mo‘jiza
	"ь е": "y e",	# Special rule: браконьер -> brakonyer
	"ъ е": "y e",	# Special rule: объект -> obyekt
	"а" : "a",
	"б" : "b",
	"д" : "d",
	"е" : "e",
	"ф" : "f",
	"г" : "g",
	"ҳ" : "h",
	"и" : "i",
	"ж" : "j",
	"к" : "k",
	"л" : "l",
	"м" : "m",
	"н" : "n",
	"о" : "o",
	"п" : "p",
	"қ" : "q",
	"р" : "r",
	"с" : "s",
	"т" : "t",
	"у" : "u",
	"в" : "v",
	"х" : "x",
	"й" : "y", 
	"з" : "z",
	"ў" : "o ‘",
	"ғ" : "g ‘",
	"ш" : "s h",
	"ч" : "c h",
	"я" : "y a",
	"ю" : "y u",
	"ё" : "y o",
	"э" : "e",
	"ъ" : "’" ,
	"ь" : "0",
}

upper_case = {
	"Ў Ъ" : "O ‘",	# SPECIAL RULE: МЎЪЖИЗА ->  MO‘JIZA
	"Ь Е": "Y e",	# SPECIAL RULE: БРАКОНЬЕР -> BRAKONYER
	"Ъ Е": "Y e",	# SPECIAL RULE: ОБЪЕКТ -> OBYEKT
	"А" : "A",
	"Б" : "B",
	"Д" : "D",
	"Е" : "E",
	"Ф" : "F",
	"Г" : "G",
	"Ҳ" : "H",
	"И" : "I",
	"Ж" : "J",
	"К" : "K",
	"Л" : "L",
	"М" : "M",
	"Н" : "N",
	"О" : "O",
	"П" : "P",
	"Қ" : "Q",
	"Р" : "R",
	"С" : "S",
	"Т" : "T",
	"У" : "U",
	"В" : "V",
	"Х" : "X",
	"Й" : "Y", 
	"З" : "Z",
	"Ў" : "O ‘",
	"Ғ" : "G ‘",
	"Ш" : "S h",
	"Ч" : "C h",
	"Я" : "Y a",
	"Ю" : "Y u",
	"Ё" : "Y o",
	"Э" : "E",
	"Ъ" : "’" ,
	"Ь" : "0",
}


lower_vowels = [ "а", "е", "и", "о", "у", "ў", "я", "э", "ё", "ю"];
lower_consonants = ["б", "д", "ф", "г", "ҳ", "ж", "к", "л", "м", "н", "п", "қ", "р", "с", "т", "в", "х", "й", "з", "ғ", "ш", "ч", "ь", "ъ"];

upper_vowels = [ "А", "Е", "И", "О", "У", "Ў", "Я", "Э", "Ё", "Ю"];
upper_consonants = ["Б", "Д", "Ф", "Г", "Ҳ", "Ж", "К", "Л", "М", "Н", "П", "Қ", "Р", "С", "Т", "В", "Х", "Й", "З", "Ғ", "Ш", "Ч", "Ь", "Ъ"];

vowels = lower_vowels + upper_vowels
consonants = lower_consonants + upper_consonants

cyrillic_uppercase = upper_vowels + upper_consonants
cyrillic_lowercase = lower_vowels + lower_consonants

latin_uppercase = ['’', '‘', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
latin_lowercase = ['’', '‘', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

latin = latin_lowercase + latin_uppercase
cyrillic = cyrillic_lowercase + cyrillic_uppercase