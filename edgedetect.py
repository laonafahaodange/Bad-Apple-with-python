import cv2
import matplotlib.pyplot as plt
import threading
import multiprocessing

class myThread (multiprocessing.Process):
    def __init__(self, startFrame, stopFrame,frames_save_path):
        multiprocessing.Process.__init__(self)
        self.startFrame = startFrame
        self.stopFrame = stopFrame
        self.frames_save_path=frames_save_path
    def run(self):
        for num in range(self.startFrame, self.stopFrame + 1):
            img = cv2.imread(self.frames_save_path + 'frame' + str(num) + '.jpg', cv2.IMREAD_GRAYSCALE)
            imgCanny = cv2.Canny(img, 50, 150)
            imgCanny = 255 - imgCanny
            plt.axis('off')
            plt.imshow(imgCanny, cmap='gray')
            plt.savefig('edgeimg\\'+str(num) + '.jpg', dpi=300)  # ,bbox_inches = 'tight')
            print(num)
        print("Convert finished.")


# def edgeDtectCanny(frames_save_path, frame_count):
#     for num in range(0, frame_count + 1):
#         img = cv2.imread(frames_save_path + 'frame' + str(num) + '.jpg', cv2.IMREAD_GRAYSCALE)
#         imgCanny = cv2.Canny(img, 50, 150)
#         imgCanny = 255 - imgCanny
#         plt.imshow(imgCanny,cmap='gray')
#         plt.savefig(str(num) + '.jpg',dpi=300)#,bbox_inches = 'tight')
#         print(num)
#     print("Convert finished.")


if __name__ == '__main__':
    frames_save_path = 'img\\'
    frame_count = 1036#图片数目，根据实际情况修改
    thread1=myThread(0,200,frames_save_path)#线程1负责索引从0到2000的图片，下面同理，可以根据实际情况修改线程数目
    thread2 = myThread(201, 400, frames_save_path)
    thread3 = myThread(401, 600, frames_save_path)
    thread4 = myThread(601, 800, frames_save_path)
    thread5 = myThread(801, 1000, frames_save_path)
    thread6 = myThread(1001, frame_count, frames_save_path)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()

    #edgeDtectCanny(frames_save_path, frame_count)
