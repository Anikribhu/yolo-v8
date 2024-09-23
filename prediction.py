from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("F:/YoloV8/runs/detect/train/weights/best.pt")

# Run inference on 'bus.jpg' with arguments
model.predict("https://www.coe.int/documents/61989255/67584870/Physical_790887175.jpg/9d511894-eaf6-688e-9eab-51b43dffb554?t=1591372186000", save=True, show =True, imgsz=320, conf=0.5)
