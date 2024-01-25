from super_gradients.training import models
import torch

yolo_nas_l = models.get("yolo_nas_l", pretrained_weights="coco")

url = "Queen.webp"
device = 'cuda' if torch.cuda.is_available() else "cpu"     #use gpu / cpu (will default to cpu if cuda is nota available) 
yolo_nas_l.to(device).predict(url, conf=0.2).show() # this sets the conf to =0.25 meaning the confidence threshold is 0.25