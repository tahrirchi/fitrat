import hfst_dev as hfst
from ..utils import cascade, list_to_group, regex_mapper
from .alphabet import (
    mapping_lower,
    mapping_upper,
    consonants,
    vowels,
    latin_uppercase,
    latin,
    cyrillic,
)


def ts_rule() -> hfst.HfstTransducer:
    ts_rule_1 = hfst.regex(f'[ ц ] -> [ s ], [ Ц ] -> [ S ] || {list_to_group(consonants)} _ , .#. _, " " _ ')
    ts_rule_2 = hfst.regex(f"[ ц ] -> [ t s ], Ц -> [ T S ] || {list_to_group(vowels)} _")

    return cascade(ts_rule_1, ts_rule_2)


def ye_rule() -> hfst.HfstTransducer:
    return hfst.regex(f'[ е ] -> [ y e ], Е -> [ Y е ] || {list_to_group(vowels)} _ , .#. _, " " _')


def normalize_digraph_case() -> hfst.HfstTransducer:
    # If Sh is the ending of the word, then it must be SH
    normalize_h_1 = hfst.regex(f"[ h ] -> [ H ] || [ C | S ] _ \[{list_to_group(latin + cyrillic)}]")
    # If Sh is followed by any uppercase Latin letter, then it must be SH
    normalize_h_2 = hfst.regex(f"[ h ] -> [ H ] || [ C | S ] _ [{list_to_group(latin_uppercase)}]")

    # Same rule for Ye, Yo, Yu, Ya
    normalize_vowel_1 = hfst.regex(f"o -> O, e -> E, u -> U, a -> A || Y _ \{list_to_group(latin + cyrillic)}")
    normalize_vowel_2 = hfst.regex(f"o -> O, e -> E, u -> U, a -> A || Y _ {list_to_group(latin_uppercase)}")

    return cascade(normalize_h_1, normalize_h_2, normalize_vowel_1, normalize_vowel_2)


def compile_model() -> hfst.HfstTransducer:
    lower_model = cascade(*regex_mapper(mapping_lower))
    upper_model = cascade(*regex_mapper(mapping_upper))
    model = cascade(ts_rule(), ye_rule(), lower_model, upper_model, normalize_digraph_case())
    model.convert(hfst.ImplementationType.HFST_OL_TYPE)

    return model
