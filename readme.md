操作顺序：  
1. 将视频放入与代码同一目录，运行video2frame.py将视频分帧，保存在img文件夹中  
2. 运行edgedetect.py对img文件夹中的图片进行边缘检测以及像素反转保存到edgeimg文件夹中，由于当时图片比较多我就用了多线程  
3. 运行frame2video.py将帧合成视频  
4. 关于BGM的问题，BGM是要后期剪辑视频的时候单独添加音轨