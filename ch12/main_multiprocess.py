from multiprocessing import Pool
import os
import time

def f(x):
    start = time.time()
    t=3
    while time.time()-start < t:
        pass
    return x*x

def main():
    start = time.perf_counter()

    print(os.cpu_count())
    with Pool() as p:
        print(p.map(f, range(10)))
    # f(3)
    end = time.perf_counter()
    print(f"{end-start:.3}s")

if __name__ == '__main__':
    main()