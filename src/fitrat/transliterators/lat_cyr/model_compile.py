import hfst_dev as hfst
from ..utils import (
    list_to_group, 
    cascade,
    regex_mapper,
)
from .alphabet import (
    mapping_lower,
    mapping_upper,
    vowels
)

def e_rule() -> hfst.HfstTransducer:
    return hfst.regex(f"e -> э, E -> Э || {list_to_group(vowels)} _ , .#. _, \"-\" _ ")


# def ts_rule() -> hfst.HfstTransducer:
#     return hfst.regex(f"[ t s ] -> ц, [ T S ] -> Ц || {list_to_group(vowels)} _")


# def tokenize_using_alphabet(word):
#     """
#     Tokenizing the word into non-divisible alphabets
#         shisha -> sh i sh a
#         chorshanba -> ch o r sh a n b a
#         soppa-sog' -> s o p p a "-" s o g'
#     """

#     # Get all non divisible symbols from our mappings
#     symbols = list(mapping_lower.keys()) + ['"-"']
#     return " ".join(re.findall('|'.join(symbols), word))


# def tokenize_word(word):
#     return " ".join(list(word)).replace('-', '"-"')


# def compile_model() -> hfst.HfstTransducer:
#     print("Compiling the model...")
#     lower_model = disjunct(*xfst_mapper(mapping_lower))
#     upper_model = disjunct(*xfst_mapper(mapping_upper))

#     model = disjunct(lower_model, upper_model)
#     model.repeat_plus()

#     exceptions_model = disjunct(
#         *xfst_mapper(
#             mapping=exceptions, 
#             key_tokenizer=tokenize_using_alphabet, 
#             value_tokenizer=tokenize_word
#         )
#     )

#     optional = model.copy()
#     optional.optionalize()

#     exceptions_model.concatenate(optional)
#     exceptions_model.priority_union(model)
#     exceptions_model.convert(hfst.ImplementationType.HFST_OL_TYPE)

#     exceptions_model.write_to_file("test.hfst")

#     return exceptions_model



def model_compile() -> hfst.HfstTransducer:
    lower_model = cascade(*regex_mapper(mapping_lower))
    upper_model = cascade(*regex_mapper(mapping_upper))

    model = cascade(e_rule(), lower_model, upper_model)
    
    model.convert(hfst.ImplementationType.HFST_OL_TYPE)

    # model.write_to_file("model/test-old.hfst")

    return model