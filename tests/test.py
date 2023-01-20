import json
from time import perf_counter

s = perf_counter()
from fitrat import Transliterator, Type
e = perf_counter()
delta = e - s


def tsv_to_dict(filepath: str) -> dict:
    dick = {}
    with open(filepath) as f:
        data = f.read()

    rows = data.split("\n")[1:]
    for row in rows:
        key, value = row.split("\t")
        dick[value] = key

    return dick


def dict_to_tsv(filepath: str, d: dict):
    data = "\n".join([f"{k}\t{v}" for k, v in d.items()])
    with open(filepath, mode="w") as f:
        f.write(data)


def dict_to_json(filepath: str, d: dict):
    with open(filepath, mode="w") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)


exceptions = {}

container = [
    tsv_to_dict(f"{i}.tsv") 
    for i in ("hard", "soft", "ts", "yayoyu")
]

t = Transliterator(to=Type.CYR)

GOOD = "ХАРОШ"
BAD = "ВЫСРАЛ"
stats = {GOOD: 0, BAD: 0}

for d in container:
    for k, v in d.items():
        res = t.convert(k)
        flag = GOOD if res == v else BAD
        stats[flag] += 1

        if flag == BAD:
            # print(f"{flag:6} | {res:15} | {v}")

            if k in exceptions:
                if exceptions[k] != v:
                    print(f"'{k}' is already exists with value '{exceptions[k]}', new value '{v}'")
            else:
                exceptions[k] = v

print("-" * 30)
print(stats)
print(len(exceptions))
print("Time taken to load the fitrat:", round(delta, 5), "seconds")

# ------ STATS ------
# -------------------
# Rule type: [ a b c ] -> [ a b c ], [ a b c ] -> [ a b c ]
# Time taken to load: 27.67515 seconds
# BAD: 561
# --------------------
# Rule type: [ a b c ] -> [ a b c ] .o. [ a b c ] -> [ a b c ]
# Time taken to load: 307.43768 seconds
# BAD: 550
# Note: ultra slow lookups
# --------------------
# Rule type: [abc] -> [abc], [abc] -> [abc]
# Time taken to load: 23.29744 seconds
# BAD: 14
# --------------------
# Rule type: [abc] -> [abc] .o. [abc] -> [abc]
# Time taken to load: 59.03468 seconds
# BAD: 11
# ---------------------
# Rule type: regex([abc] -> [abc]).compose([abc] -> [abc])
# Time taken to load: 44.5575 seconds
# BAD: 11

# dict_to_json("exceptions.json", exceptions)
# dict_to_tsv("exceptions.tsv", exceptions)
