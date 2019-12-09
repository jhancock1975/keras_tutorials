import numpy as np

def arr_rand_sample(arr, n=5):
    """random sample of numpy array elements
    @param arr: input array
    @param n: number of samples to return, default 5
    @return array of n elements sampled from arr
    """
    return arr[np.random.randint(np.size(arr, axis=0), size = (n))]

def arr_stats(arr, n=5):
    """print some statistics on an array
    @parm arr: input array
    @param n: number of samples to return, default 5
    @return: shape and random sample of array
    """
    return arr.shape, arr_rand_sample(arr)
