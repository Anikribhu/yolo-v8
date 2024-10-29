from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("D:/YoloV8/runs/detect/train2/weights/best.pt")

# Run inference on 'bus.jpg' with arguments
model.predict("https://wordpress.wbur.org/wp-content/uploads/2014/03/0317_fan-violence_cog-1000x547.jpg", save=True, show =True, imgsz=640, conf=0.5)
