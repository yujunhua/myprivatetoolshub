from moviepy.editor import *

video_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface/video/2.mp4"
videoout_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface/video/3.mp4"

video = VideoFileClip(video_path)
video_out = video.subclip(0, 0.1) # 0.1s
video_out.to_videofile(videoout_path)
