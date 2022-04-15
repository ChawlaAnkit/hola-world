import multiprocessing
import os
from multiprocessing import Process
import random
import shutil

filenames = random.choice(os.listdir("C:/Users/Administrator/pypy/Image_data"))
os.mkdir("test_image")
def do_smth():
    print("entering into a function")
    for i in range(10):
        print("hello")
        output_p = os.path.join(os.getcwd(),f"test_image/{foldername}/{i}.jpg")
        print(output_p)
        shutil.copy(os.path.join(dest_path, os.listdir(dest_path)[0]), output_p)
pro=[]
cunt = 0
if __name__== "__main__":
    for fname in filenames:
        
        foldername = filenames.split(".")[0]
        if not os.path.exists(f"./test_image/{foldername}"):
            os.mkdir(f"./test_image/{foldername}")
        dest_path = os.path.join(os.getcwd(),f"test_image/{foldername}")
        # print(dest_path)
        source_path = f"C:/Users/Administrator/pypy/Image_data/{filenames}"
        # image_color = cv2.imread(source_path,-1)
        # cv2.imshow("hello",image_color)
        # cv2.waitKey(0)

        print("for loop started")
        shutil.copy(source_path,dest_path)
        print("process about to start")
        p = Process(target = do_smth)
        print(p)
        pro.append(p)
        pro[cunt].start()
        print("reaching")
        pro[cunt].join()
        cunt += 1
    # for pr in pro:
    #     print("end is near")
    #     pr.join()
