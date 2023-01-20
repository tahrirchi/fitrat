import hfst_dev as hfst
from ..utils import (
    cascade, 
    list_to_group, 
    regex_mapper, 
    disjunct,
    regex_map_new,
    gen_lexc_mapping
)
from .alphabet import (
    exceptions,
    mapping_lower,
    mapping_upper,
    vowels
)

def e_rule() -> hfst.HfstTransducer:
    return hfst.regex(f"e -> э, E -> Э || {list_to_group(vowels)} _ , .#. _, \"-\" _ ")


def ts_rule() -> hfst.HfstTransducer:
    return hfst.regex(f"[ t s ] -> ц, [ T S ] -> Ц || {list_to_group(vowels)} _")


def compile_model() -> hfst.HfstTransducer:
    lower_model = cascade(*regex_mapper(mapping_lower))
    upper_model = cascade(*regex_mapper(mapping_upper))
    exceptions_model = disjunct(*regex_map_new(exceptions))
    # exceptions_model = regex_map_new(exceptions)
    
    # exceptions_model = gen_lexc_mapping(exceptions)
    # if exceptions_model is None:
    #     model = cascade(e_rule(), lower_model, upper_model)
    # else:
    #     model = cascade(e_rule(), exceptions_model, lower_model, upper_model)
    
    model = cascade(e_rule(), exceptions_model, lower_model, upper_model)
    # model = cascade(e_rule(), lower_model, upper_model)
    model.convert(hfst.ImplementationType.HFST_OL_TYPE)

    return model
