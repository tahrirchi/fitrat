from hfst_dev import HfstTransducer, regex, compile_lexc_script, compile_lexc_file


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


def regex_map_new(mapping: dict) -> list:
  f = lambda x: ' '.join(list(x)).replace('-', '"-"')
  # f = lambda x: x.replace('-', '"-"')

  # joiner = " .o. "
  # joiner = ", "

  # return regex(joiner.join([f"[{f(key)}] -> [{f(value)}]" for key, value in mapping.items()]))
  return [regex(f"[{f(key)}] -> [{f(value)}]" for key, value in mapping.items())]

def gen_lexc_mapping(mapping: dict) -> HfstTransducer:
  from io import StringIO
  f = lambda x: x.replace('-', '"-"')
  lexc = "Multichar_Symbols\nLEXICON Root\n\nNoun ;\n\nLEXICON Noun\n\n"
  lexc += "\n".join([f"{k}:{v} #;" for k, v in mapping.items()])
  
  with open("test.lexc", mode="w") as f:
    f.write(lexc)

  return compile_lexc_file("test.lexc")

  # return compile_lexc_script(lexc, output=StringIO)
  # return compile_lexc_script(lexc)
