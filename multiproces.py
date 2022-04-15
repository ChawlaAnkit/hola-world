import multiprocessing 
import time
from multiprocessing import Process


def do_smth(second):
    print(f"Process is sleeping for {second}")
    time.sleep(second)
    print(f"Done sleeping for {second}" + " seconds")

    
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     f1 = executor.submit(do_smth , 1)
#     print(f1)





if __name__ =="__main__":

    
    pro = []
    for n in range(10):
        a= time.time()
        p = Process(target = do_smth, args =[5])
        print("buzz world")
        pro.append(p)
        pro[n].start()
    
    for pr in pro:
        pr.join()
    b= time.time()
    print(f"finally {b-a:.4f}")  

    
    



