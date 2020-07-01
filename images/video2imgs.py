"""
要用到下面的 ffmpeg 和 ffprobe 命令，首先要先下载好两个文件并放在代码统计目录下
下载地址 ： http://ffmpeg.org/download.html
两个文件： ffmpeg ffprobe
"""
import os
import sys
import subprocess
import json

ffprobe_path = os.path.join(os.getcwd(), "ffprobe")
ffmpeg_path = os.path.join(os.getcwd(), "ffmpeg")


# 定义获取视频信息的函数，参数是视频文件
def getVideoProbeInfo(filename):
    # 获取视频信息的命令行
    command = [ffprobe_path, "-loglevel", "quiet", "-print_format", "json", "-show_format", "-show_streams", "-i",
               filename]
    # 执行命令行
    result = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = result.stdout.read()
    # 返回json结果
    return str(out.decode('utf-8'))

# 通过FFmpeg将视频的每帧保存成图片
def fullVideoProc(filename, output_dir, sec_idx, end_idx, allFrames = True, framesPerSec = 1):
    if allFrames == True:
        # 这个命令行就是上面介绍的
        command = [ffmpeg_path,"-y","-i",filename, "-ss", str(sec_idx), "-t", str(end_idx), "-q:v", "2", "-f",
                   "image2",output_dir+"%6d.jpg"]
    else:
        # 这个命令行多了一个-r，传入的framesPerSec值是1，目的是每秒只取一帧画面，可以加速处理，但是由于抛弃了很多帧画面，结果会有遗漏
        command = [ffmpeg_path, "-y", "-i", filename, "-ss", str(sec_idx), "-t", str(end_idx), "-r", str(framesPerSec), "-q:v", "2", "-f",
                   "image2", output_dir + "%6d.jpg"]
    # 执行命令行
    result = subprocess.Popen(command,shell=False,stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    out = result.stdout.read()
# 从传入的json中返回format下的duration字段值，单位是秒
def getDuration(VIDEO_PROBE):
    data = json.loads(VIDEO_PROBE)["format"]['duration']
    return data

if __name__ == '__main__':
    # 参数src指定要解析的视频
    videoPath = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface/video/1.mp4"
    dstpath = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface\jpg/"
    total_time = []

    # 先获取视频文件的信息，json格式
    VIDEO_PROBE = getVideoProbeInfo(videoPath)
    # 得到视频文件的时长，秒为单位
    sec = float(getDuration(VIDEO_PROBE))

    print(sec)

    # 通过FFmpeg将视频每帧解出来
    fullVideoProc(videoPath, dstpath, 0, sec, True)