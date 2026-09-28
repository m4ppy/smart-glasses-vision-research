from ultralytics import YOLO


def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data=r"dataset_80_10_10\data.yaml",
        epochs=100,
        imgsz=640,
        device=0,
        optimizer="AdamW",
        degrees=20,
        name="yolov8n_80_10_10_rotation20"
    )


if __name__ == "__main__":
    main()