import cv2
video_read_test = cv2.VideoCapture("./Image_folder/img_0002/%01d.jpg")

fps= video_read_test.get(5)
print(f"FPS = {fps}")
frame_count = video_read_test.get(7)
print(f"Frame Count = {frame_count}")
frame_width = int(video_read_test.get(3))
frame_height = int(video_read_test.get(4))
size = (frame_width, frame_height)
print(size)
print(video_read_test.isOpened())
result = cv2.VideoWriter("./Image_folder/img_0002/video.avi",
                        cv2.VideoWriter_fourcc(*'MJPG'),
                        fps, size)

while(video_read_test.isOpened()):
    ret, frame = video_read_test.read()
    if(ret == True):
        result.write(frame)
    else:
        print("Stream disconected")
        break
video_read_test.release()
result.release()


cv2.destroyAllWindows()