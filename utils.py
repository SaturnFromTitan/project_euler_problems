import time


def timeit(func):
    def timed(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        elapsed_in_ms = (time.time() - start) * 1000
        print(f"Computation Time  {elapsed_in_ms:2.3f}ms")
        return result
    return timed
