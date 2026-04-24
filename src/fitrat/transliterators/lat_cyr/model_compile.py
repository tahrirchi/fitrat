import hfst

from ..utils import cascade, list_to_group, regex_mapper
from .alphabet import mapping_lower, mapping_upper, vowels


def e_rule() -> hfst.HfstTransducer:
    return hfst.regex(f'e -> э, E -> Э || {list_to_group(vowels)} _ , .#. _, "-" _ ')


def model_compile() -> hfst.HfstTransducer:
    lower_model = cascade(*regex_mapper(mapping_lower))
    upper_model = cascade(*regex_mapper(mapping_upper))

    model = cascade(e_rule(), lower_model, upper_model)

    model.convert(hfst.ImplementationType.HFST_OL_TYPE)

    return model
