import multiprocessing 
import time
from multiprocessing import Process
m=0

import os
import random
import shutil
import random
import cv2
import time
import multiprocessing
from multiprocessing import Process,Pool

str = time.time()
filenames = random.sample(os.listdir("C:/Users/Administrator/pypy/Image_data"),1000)
# if os.path.exists("image_folder"):
#     shutil.rmtree("image_folder")
    
def cop_rpeat(foldername,dest_path,k):
    print(f"{foldername}")
    print(f"{dest_path}")
print("main function about to start")
if __name__== "__main__":
    for fname in filenames:
        
        foldername = fname.split(".")[0]
        print(foldername)
        # git testing purpose