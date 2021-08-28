import cv2

def frame2Video(fps,size,frameNum):
    video = cv2.VideoWriter("outputvideo.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)#输出视频的格式建议用avi
    for num in range(0,frameNum+1):
        img=cv2.imread('edgeimg\\'+str(num)+'.jpg')
        video.write(img)
        print(num)
    video.release()
    cv2.destroyAllWindows()
    print("Convert finished.")

if __name__ == '__main__':
    fps=30
    size=(1920,1440)
    frameNum=1036
    frame2Video(fps,size,frameNum)