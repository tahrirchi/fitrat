import hfst_dev as hfst

def cascade(*args):
	'''
	  Input:
	    args - iterable of transducers	hfst.HfstTransducer 
	  Output:
	    fst - composed transducer by the order they listed in iterable of type hfst.HfstTransducer 
	'''
	fst = args[0]
	for tr in args[1:]:
		fst.compose(tr)
	return fst

def list_to_group(ls):
	'''
	  Input:
	    ls - list of symbols
	  Output:
	    union - a string union group of symbols according to XFST syntax
	'''
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
    return [hfst.regex(f"[{f(key)}] -> [{f(value)}]") for key, value in mapping.items()]