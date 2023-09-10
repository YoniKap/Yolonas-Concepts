from super_gradients.training import models
import torch

yolo_nas_l = models.get("yolo_nas_l", pretrained_weights="coco")

input_video_path = "video.mp4"
output_video_path = "detected.mp4"
min_confidence_threshold = 0.6
device = 'cuda' if torch.cuda.is_available() else "cpu"     #use gpu / cpu (will default to cpu if cuda is nota available) 
yolo_nas_l.to(device).predict(input_video_path,conf=min_confidence_threshold).save(output_video_path)


