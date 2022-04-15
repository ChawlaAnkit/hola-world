import os
import random
import shutil
import random
import cv2
import time
import multiprocessing
from multiprocessing import Process

str = time.time()
filenames = random.sample(os.listdir("C:/Users/Administrator/pypy/Image_data"),1000)
if os.path.exists("image_folder"):
    shutil.rmtree("image_folder")
    
os.mkdir("image_folder")

print("main function about to start")
if __name__== "__main__":
    for fname in filenames:
        
        foldername = fname.split(".")[0]
        if not os.path.exists(f"./image_folder/{foldername}"):
            os.mkdir(f"./image_folder/{foldername}")
        dest_path = os.path.join(os.getcwd(),f"image_folder/{foldername}")
        # print(dest_path)
        source_path = f"C:/Users/Administrator/pypy/Image_data/{fname}"
        # image_color = cv2.imread(source_path,-1)
        # cv2.imshow("hello",image_color)
        # cv2.waitKey(0)

        print("for loop started")
        shutil.copy(source_path,dest_path)
def loop_cont (dest, source):
    shutil.copy(source, dest)

    


end = time.time()
print(f"Total time {end-str}")

dest[]

for addr in dest_pa:
    dest.append(addr)
    
pool = multiprocessing.Pool()
pool.map(loop_cont, (dest, source)