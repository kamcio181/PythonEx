from ex3 import MapReduce
from collections import Counter


def count_words(file):
    try:
        return list(Counter(open(file, 'r').read().replace('\n', ' ').replace(',', '').replace('.', '').
                            replace(';', '').lower().split(' ')).items())
    except FileNotFoundError:
        print('File %s not found' % file)
        return list()


def reduce(item_to_reduce):
    word, count_list = item_to_reduce
    return word, sum(count_list)


# paths = input("Enter file paths separated by space\n").split(sep=' ')
paths = ['text1.txt', 'text2.txt', 'text3.txt', 'text4.txt', 'text5.txt']
map_reduce = MapReduce(paths)

counted_words = map_reduce.map_reduce(count_words, reduce, 4)
print([x[0] for x in Counter(dict(counted_words)).most_common(20)])
