# YOLO-Based Fingerspelling Recognition

This study investigates YOLO-based object detection for recognizing 26 alphabet fingerspelling hand shapes in smart-glass-oriented vision scenarios.

The study compares YOLOv8 and YOLOv12 and includes an additional YOLOv8n experiment to analyze training convergence and class-wise recognition errors.

## Research Scope

- 26-class alphabet fingerspelling recognition
- YOLO-based object detection
- YOLOv8 and YOLOv12 performance comparison
- Additional YOLOv8n training and evaluation
- Training convergence analysis
- Class-wise confusion analysis
- Smart-glass-oriented vision applications

## Additional YOLOv8n Experiment

A separate YOLOv8n experiment was conducted for 100 epochs using a custom 80/10/10 train-validation-test split.

The experiment includes:

- Training configuration
- Dataset split generation
- Independent test evaluation
- Epoch-wise mAP results
- Normalized confusion matrix

See:

`experiments/yolov8n-100epoch/`

## Key YOLOv8n Results

### Validation

- mAP50: 0.99223
- mAP50-95: 0.84868

### Independent Test

- mAP50: 0.988
- mAP50-95: 0.843

## Repository Structure

```text
yolo-fingerspelling-recognition/
├── README.md
├── experiments/
│   └── yolov8n-100epoch/
└── paper/
```

## Publication

Publication information is available in:

`paper/README.md`