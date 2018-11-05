import math


def paginate(seq, pages=None, items=None):
    if pages is not None:
        return split(seq, math.ceil(len(seq)/pages))

    return split(seq, items)


def split(seq, items):
    seq = list(seq)
    return [seq[i: i + items] for i in range(0, len(seq), items)]


print(paginate(range(10), pages=2))
print(paginate('abcdefghij', pages=3))
print(paginate(range(10), items=2))
print(paginate('abcde', items=3))
print(paginate(range(10), 2, 7))