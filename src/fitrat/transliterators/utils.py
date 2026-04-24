import hfst


def cascade(*args):
    """Compose transducers in sequence.

    Args:
        args: iterable of hfst.HfstTransducer

    Returns:
        Composed transducer.
    """
    fst = args[0]
    for tr in args[1:]:
        fst.compose(tr)
    return fst


def list_to_group(ls):
    """Convert a list of symbols to an XFST union group string.

    Args:
        ls: list of symbols

    Returns:
        A string union group of symbols according to XFST syntax.
    """
    return "[" + " | ".join(ls) + "]"


def regex_mapper(mapping: dict) -> list:
    """Create regex transducers that replace mapping keys to mapping values.

    Args:
        mapping: dictionary of mapping symbols

    Returns:
        List of regex transducers.
    """

    def _escape(x):
        return x.replace("-", '"-"')

    return [hfst.regex(f"[{_escape(key)}] -> [{_escape(value)}]") for key, value in mapping.items()]
