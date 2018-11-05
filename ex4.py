from collections import Counter
import multiprocessing as mp

# paths = input('Enter paths to files separated with space').split(sep=' ')
paths = ['text1.txt', 'text2.txt', 'text3.txt', 'text4.txt', 'text5.txt']
print(paths)
finalResult = Counter()


def map_reduce(map_func, reduce_func, num_workers):
    pool = mp.Pool(processes=num_workers)
    global paths
    results = [pool.apply_async(map_func, args=(file,)) for file in paths]  # how many times?
    results = [pool.apply_async(reduce_func, args=(result.get(),)) for result in results]
    for result in results:
        print(result.get())
    global finalResult
    print(finalResult)


def count_words_in_file(file):
    return Counter(open(file, 'r').read().replace('\n', ' ').replace(',', '').replace('.', '').replace(';', '')
                   .lower().split(' '))


def reduce(counter):
    global finalResult
    print('reduce c')
    print(counter)
    finalResult += counter
    print('reduce f')
    print(finalResult)



map_reduce(count_words_in_file, reduce, 1)
