import cv2

def video2frame(videos_path, frames_save_path):
    vidcap = cv2.VideoCapture(videos_path)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imencode('.jpg', image)[1].tofile(frames_save_path + "/frame%d.jpg" % count)
        success, image = vidcap.read()
        count += 1
        print(count)
    print("Convert finished.")


if __name__ == '__main__':
    videos_path = 'test.flv'#修改成你视频的名字
    frames_save_path = 'img'
    video2frame(videos_path, frames_save_path)
