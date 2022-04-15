   
import time
import multiprocessing

def do_smth():
    print("sleeping for 1 second")
    time.sleep(5)
    print("Done sleeping")


if __name__ == "__main__": 
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=do_smth)
    p2 = multiprocessing.Process(target=do_smth)
    p1.start()
   
    p2.start()
    p1.join()
    p2.join()
    

    print(f"processes are alive {p2.is_alive()}")

    finish = time.perf_counter()
    print(f"total time taken {finish - start} second")


        

