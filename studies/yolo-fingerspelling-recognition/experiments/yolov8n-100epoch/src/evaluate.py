from ultralytics import YOLO


def main():
    model = YOLO(
        r"runs\detect\yolov8n_80_10_10_rotation20\weights\best.pt"
    )

    model.val(
        data=r"dataset_80_10_10\data.yaml",
        split="test",
        device=0
    )


if __name__ == "__main__":
    main()