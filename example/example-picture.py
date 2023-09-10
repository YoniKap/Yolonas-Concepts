from super_gradients.training import models

yolo_nas_l = models.get("yolo_nas_l", pretrained_weights="coco")

url = "Queen.webp"
yolo_nas_l.predict(url, conf=0.25).show() # this sets the conf to =0.25 meaning the confidence threshold is 0.25