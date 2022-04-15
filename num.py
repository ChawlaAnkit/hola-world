from multiprocessing import Pool
import time
from functools import partial


d="99"
e="100"   
l=[]    
p=[]
k=[0]
def sleeping(d,e,k):
    print("function starts")
    time.sleep(1)
    print("done sleeping")
    
    
    print(d)
    print(e)
if __name__=="__main__":
    str = time.time()
    with Pool() as pool:
        for n in range(10):
            
            l.extend(k)
            k[0]=k[0]+1
            # buz=partial(sleeping,d,e)
        pool.map(sleeping,l,e)
        

    # for i in range(10):
    #     p[i].join()
    
    print(l)
    pool.close()
    end = time.time()
    print(f"Total time {end-str}")
    

