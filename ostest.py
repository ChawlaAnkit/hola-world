#! /usr/bin/python


import os
import random
import shutil
import time
from concurrent.futures import ProcessPoolExecutor
from cv2 import cv2
from tqdm import tqdm



def world(fname):

    foldername = fname.split(".")[0]
    if not os.path.exists(fr"./image_folder/{foldername}"):
        os.mkdir(fr"./image_folder/{foldername}")
    dest_path = os.path.join(os.getcwd(), f"image_folder/{foldername}")
    source_path = fr"C:/Users/Administrator/pypy/Image_data/{fname}"
    shutil.copy(source_path,dest_path)
    for i in range(800):
        output_p = os.path.join(os.getcwd(),fr"image_folder\{foldername}\{i}.jpg")
        shutil.copy(os.path.join(dest_path, os.listdir(dest_path)[0]), output_p)
    video_read_test = cv2.VideoCapture(fr"./Image_folder/{foldername}/%01d.jpg")
    fps= video_read_test.get(5)
    frame_width = int(video_read_test.get(3))
    frame_height = int(video_read_test.get(4))
    size = (frame_width, frame_height)
    result = cv2.VideoWriter(fr"./Image_folder/{foldername}/video.avi",cv2.VideoWriter_fourcc(*'MJPG'),fps, size)

    while video_read_test.isOpened():
        ret, frame = video_read_test.read()
        if ret is True:
            result.write(frame)
        else:
            break
    video_read_test.release()
    result.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    print("main function about to start")
    filenames = random.sample(os.listdir(r"C:/Users/Administrator/pypy/Image_data"), 1000)
    if os.path.exists("./image_folder"):
        shutil.rmtree("image_folder")
    start = time.time()
    os.mkdir("image_folder")

    with ProcessPoolExecutor(max_workers=5) as exe:
        _ = list(tqdm(exe.map(world,filenames), total=1000))
    end = time.time()
    print(f"Total time {end-start}")
