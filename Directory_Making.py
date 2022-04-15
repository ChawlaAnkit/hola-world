"""If you check it in the Task Manager you will see that CPU Utilization os 100%. 
Means we are using the full capability of the machine."""

import os
import random
import shutil
import random
from concurrent.futures import ProcessPoolExecutor
import time
from tqdm import tqdm
import cv2


def main(dirpath):  #Create directory
    dirName = 'Image_folder'

    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName,  " Created ")

        filenames = random.sample(os.listdir(dirpath), 1000)
        return filenames

    except FileExistsError:
        print("Directory ", dirName,  " already exists")


def copy(fname):

    dirpath = r"C:/Users/Administrator/pypy/Image_data"
    folder_name = fname.split('.')[0]
    os.mkdir('.\Image_folder\{0}'.format(folder_name))
    source_file = os.path.join(dirpath, fname)
    dest_path = r'C:\Users\Administrator\pypy\Image_folder\{0}'.format(
        folder_name)
    shutil.copy(source_file, dest_path)

    output_path = r'C:\Users\Administrator\pypy\Image_folder\{}\{}.jpg'
    # print(os.listdir(dest_path)[0])

    for i in range(800):
        shutil.copy(os.path.join(dirpath, fname),
                    output_path.format(folder_name, i))
    #     shutil.copy(os.listdir(dest_path)[0], output_p.format(folder_name, i))


if __name__ == '__main__':
    start = time.time()
    dirpath = r"C:/Users/Administrator/pypy/Image_data"
    values = main(dirpath)
    print(values)
# TODO: With ProcessPoolExecutor it took around 7 mins.

    with ProcessPoolExecutor(max_workers=5) as exe:
        _ = list(tqdm(exe.map(copy,values), total=1000))

# TODO: With Thread Pool Executor total time it took around little more than 7 min

# So both the methods took almost the same time.

    # with ThreadPoolExecutor(max_workers=5) as exe:
    #     _ = list(tqdm(exe.map(copy, values), total=1000))
    end = time.time()

    print(f'Total time to run the code with Multiprocessing is : {end-start}')
