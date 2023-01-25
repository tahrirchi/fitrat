from hfst_dev import HfstTransducer, regex, compile_lexc_file
import time


def cascade(*args: HfstTransducer) -> HfstTransducer:
    """
    Input:
      args - iterable of transducers	hfst.HfstTransducer
    Output:
      fst - composed transducer by the order they listed in iterable of type hfst.HfstTransducer
    """
    fst = args[0]
    for tr in args[1:]:
        fst.compose(tr)
    return fst


def disjunct(*args: HfstTransducer) -> HfstTransducer:
    fst = args[0]
    for tr in args[1:]:
        fst.disjunct(tr)
    return fst


def list_to_group(ls: list) -> str:
    """
    Input:
      ls - list of symbols
    Output:
      union - a string union group of symbols according to XFST syntax
    """
    return "[" + " | ".join(ls) + "]"


def regex_mapper(mapping: dict) -> list:
    """
    Input:
      mapping - dictionary of mapping symbols
    Output:
      list - list of regex transducers that replace mapping keys to mapping values
    """
    # Escape character
    f = lambda x: x.replace('-', '"-"')
    return [regex(f"[{f(key)}] -> [{f(value)}]") for key, value in mapping.items()]


def xfst_mapper(mapping: dict, key_tokenizer=lambda x: x, value_tokenizer=lambda x: x) -> list:
    """
    Input:
      mapping - dictionary of mapping symbols
	    key_tokenizer - an optional function for preprocessing keys of map
      value_tokenizer - an optional function for preprocessing values of map
    Output:
      list - list of regex transducers that replace mapping keys to mapping values
    """
    return [regex(f"[{key_tokenizer(key)}]:[{value_tokenizer(value)}]") for key, value in mapping.items()]


def regex_map_new(mapping: dict) -> HfstTransducer:
    # f = lambda x: ' '.join(list(x)).replace('-', '"-"')
    # f = lambda x: x.replace('-', '"-"')
    f = lambda x: x.replace('-', '%-')

    # joiner = " .o. "
    # joiner = ", "

    # return regex(joiner.join([f"[{f(key)}] -> [{f(value)}]" for key, value in mapping.items()]))
    s = time.perf_counter()
    res = [regex(f"{f(key)}:{f(value)}") for key, value in mapping.items()]
    e = time.perf_counter()
    print("Exceptions:", len(mapping))
    print("Time taken for compiling separate exceptions:", round(e-s, 3))
    s = time.perf_counter()
    union = disjunct(*res)
    e = time.perf_counter()
    print("Time taken for disjuncting exceptions into one:", round(e-s, 3))
    return union
