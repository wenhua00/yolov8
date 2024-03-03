from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-seg.yaml')  # build a new model from YAMLmodel = YOLO('/home/tin/project/oepncv/ultralytics/ultralytics/yolov8n-seg.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n-seg.pt')  # load a pretrained model (recommended for training)
# # Train the model
results = model.train(data='/home/haoyang-22/project/event-camera/ultralytics/ultralytics/cfg/datasets/detect0209.yaml', epochs=50, imgsz=720)