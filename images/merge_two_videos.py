from moviepy.editor import *

video1_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface/video/1.mp4"
video2_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface/video/2.mp4"
videoout_path = "D:\TMP\ml/tf\YOLOv3_TensorFlow\data\demo_data\myface/video/3.mp4"

video1 = VideoFileClip(video1_path)
video2 = VideoFileClip(video2_path)
final_clip = concatenate_videoclips([video1, video2])
final_clip.to_videofile(videoout_path)
