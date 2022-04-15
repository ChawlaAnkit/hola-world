import time
from multiprocessing import Process


class Worker(Process):

    def run(self):

        print(f'In {self.name}')
        time.sleep(2)

def main():

    worker = Worker()
    print("testing")
    worker.start()

    worker5 = Worker()
    print("hello`")
    worker5.start()

    worker.join()
    worker5.join()

if __name__ == '__main__':
    str = time.time()
    main()
    fin = time.time()
    print(fin - str)