import multiprocessing as mp


def map_reduce(map_func, reduce_func, num_workers):
    pool = mp.Pool(processes=num_workers)
    results = [pool.apply_async(map_func,)]# how many times?
