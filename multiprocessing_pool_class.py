import time
import multiprocessing





def is_perfect(n):
    sum_factors = 0
    for i in range(1, n):
        if(n % i == 0):
            sum_factors = sum_factors + i
    if (sum_factors == n):
        print('{} is a Perfect number'.format(n))
if __name__=="__main__":
    tic = time.time()
    pool = multiprocessing.Pool() #write the number of processor u reqd for multiprocessing in the bracket
    pool.map(is_perfect, range(1,100000))
    pool.close()
    toc = time.time()

    print(f'Done in {toc-tic:.4f} seconds')