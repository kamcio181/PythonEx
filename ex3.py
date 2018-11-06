from multiprocessing import Pool
from itertools import chain
from collections import defaultdict


class MapReduce:

    def __init__(self, input_data):
        self.__input_data = input_data

    def map_reduce(self, map_func, reduce_func, num_workers):
        pool = Pool(processes=num_workers)
        result = pool.map_async(map_func, self.__input_data)

        mid_data = defaultdict(list)
        for key, value in chain.from_iterable(result.get()):
            mid_data[key].append(value)

        result = [result.get() for result in [pool.apply_async(reduce_func, args=(key, value)) for key, value in mid_data.items()]]
        return result

