# YOLOv8n 100-Epoch Experiment

## Environment

- GPU: NVIDIA GeForce RTX 5080 16GB
- Python: 3.11.16
- PyTorch: 2.11.0
- Ultralytics: 8.4.155

## Training

- Model: YOLOv8n
- Epochs: 100
- Image size: 640
- Batch size: 16
- Optimizer: AdamW

Detailed training parameters are available in:

`config/args.yaml`

## Results

### Validation

- mAP50: 0.99223
- mAP50-95: 0.84868

### Independent Test

- mAP50: 0.988
- mAP50-95: 0.843

## Files

- `src/train.py`: training script
- `src/evaluate.py`: independent test evaluation
- `config/args.yaml`: Ultralytics training configuration
- `data/split_manifest.csv`: exact dataset split
- `results/results.csv`: epoch-level training results
- `results/map_convergence.png`: validation mAP convergence
- `results/confusion_matrix_normalized.png`: normalized test confusion matrix