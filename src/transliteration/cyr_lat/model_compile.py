import hfst_dev as hfst
from alphabet import lower_case, upper_case, consonants, vowels, latin_uppercase, punctuation

def cascade(*args):
	fst = args[0]
	for tr in args[1:]:
		fst.compose(tr)
	return fst

def list_to_group(ls):
	return "[" + " | ".join(ls) + "]"

def list_to_group_quotes(ls):
	ls = [f"""\"{l}\"""" for l in ls if l != '%"']
	ls.append('%"')
	return "[" + " | ".join(ls) + "]"

def ts_rule():
	ts_rule_1 = hfst.regex(f'[ ц ] -> [ s ], [ Ц ] -> [ S ] || {list_to_group(consonants)} _ , .#. _, " " _ ')
	ts_rule_2 = hfst.regex(f"[ ц ] -> [ t s ], Ц -> [ T S ] || {list_to_group(vowels)} _")

	return cascade(ts_rule_1, ts_rule_2)

def ye_rule():
	ye_rule = hfst.regex(f'[ е ] -> [ y e ], Е -> [ Y E ] || {list_to_group(vowels)} _ , .#. _, " " _')
	return ye_rule


def normalize_digraph_case():
	# print(punctuation)
	normalize_h = hfst.regex(f'[ h ] -> [ H ] || [{list_to_group_quotes(punctuation)} | {list_to_group(latin_uppercase)} | .#. ] [ C | S ] _ [{list_to_group_quotes(punctuation)} | {list_to_group(latin_uppercase)} | .#. ]')
	return normalize_h


def model_compile():
	lower_model = cascade(*[hfst.regex(f"[{key}] -> [{value}]") for key, value in lower_case.items()])
	upper_model = cascade(*[hfst.regex(f"[{key}] -> [{value}]") for key, value in upper_case.items()])
	model = cascade(ts_rule(), ye_rule(), lower_model, upper_model, normalize_digraph_case())

	model.convert(hfst.ImplementationType.HFST_OL_TYPE)

	return model


