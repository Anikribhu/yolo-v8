import torch
print(torch.cuda.is_available())  # Should return True if CUDA is available
print(torch.cuda.get_device_name(0))  # Should print the name of your GPU



# yolo train data="hockey_vio-1/data.yaml" model=yolov8m.pt epochs=3 lr0=0.1 imgsz=320 conf=0.25 workers=4
# yolo task=detect mode=predict model=runs/detect/train/weights/best.pt conf=0.5 source=hockey_vio-1/test/images
# https://www.coe.int/documents/61989255/67584870/Physical_790887175.jpg/9d511894-eaf6-688e-9eab-51b43dffb554?t=1591372186000
# yolo task=detect mode=predict model=/content/runs/detect/train4/weights/best.pt conf=0.5 source=/content/hockey_vio-1/test/images