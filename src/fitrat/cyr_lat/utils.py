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
	