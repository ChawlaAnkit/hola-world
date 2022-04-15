import cv2
video_read_test = cv2.VideoCapture("sample_video.mp4")

fps= video_read_test.get(5)
print(f"FPS = {fps}")
frame_count = video_read_test.get(7)
print(f"Frame Count = {frame_count}")
print(video_read_test.isOpened())
while(video_read_test.isOpened()):
    ret, frame = video_read_test.read()
    if(ret == True):
        cv2.imshow("video",frame)
        k=cv2.waitKey(25)
        if k == 32:
            break
    else:
        break
video_read_test.release()
cv2.destroyAllWindows()
        
