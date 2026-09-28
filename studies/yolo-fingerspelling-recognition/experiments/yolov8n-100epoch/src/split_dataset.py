from pathlib import Path
import random
import shutil


SEED = 42

SOURCE_DIR = Path("dataset")
OUTPUT_DIR = Path("dataset_80_10_10")

SOURCE_SPLITS = ["train", "valid", "test"]

random.seed(SEED)


def get_class_id(label_path: Path):
    """
    이 데이터셋은 이미지당 손 객체 1개를 전제로
    첫 번째 annotation의 class id를 사용한다.
    """
    with open(label_path, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()

    if not first_line:
        return None

    return int(first_line.split()[0])


def copy_sample(image_path, label_path, split_name):
    image_output = OUTPUT_DIR / split_name / "images"
    label_output = OUTPUT_DIR / split_name / "labels"

    image_output.mkdir(parents=True, exist_ok=True)
    label_output.mkdir(parents=True, exist_ok=True)

    shutil.copy2(image_path, image_output / image_path.name)
    shutil.copy2(label_path, label_output / label_path.name)


def main():
    # class_id -> [(image_path, label_path), ...]
    samples_by_class = {}

    # 기존 train / valid / test를 모두 하나로 합침
    for split in SOURCE_SPLITS:
        image_dir = SOURCE_DIR / split / "images"
        label_dir = SOURCE_DIR / split / "labels"

        for image_path in image_dir.iterdir():
            if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
                continue

            label_path = label_dir / f"{image_path.stem}.txt"

            if not label_path.exists():
                print(f"Label missing: {image_path}")
                continue

            class_id = get_class_id(label_path)

            if class_id is None:
                print(f"Empty label: {label_path}")
                continue

            samples_by_class.setdefault(class_id, []).append(
                (image_path, label_path)
            )

    train_samples = []
    val_samples = []
    test_samples = []

    # 클래스별로 80 / 10 / 10 분할
    for class_id, samples in sorted(samples_by_class.items()):
        random.shuffle(samples)

        total = len(samples)

        train_count = int(total * 0.8)
        val_count = int(total * 0.1)

        train = samples[:train_count]
        val = samples[train_count:train_count + val_count]
        test = samples[train_count + val_count:]

        train_samples.extend(train)
        val_samples.extend(val)
        test_samples.extend(test)

        print(
            f"Class {class_id:2d}: "
            f"total={total:3d} | "
            f"train={len(train):3d} "
            f"val={len(val):3d} "
            f"test={len(test):3d}"
        )

    # 혹시 이전 실행 폴더가 있으면 제거
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    for image_path, label_path in train_samples:
        copy_sample(image_path, label_path, "train")

    for image_path, label_path in val_samples:
        copy_sample(image_path, label_path, "valid")

    for image_path, label_path in test_samples:
        copy_sample(image_path, label_path, "test")

    print("\n===== Final Split =====")
    print("Train:", len(train_samples))
    print("Valid:", len(val_samples))
    print("Test :", len(test_samples))
    print("Total :", len(train_samples) + len(val_samples) + len(test_samples))


if __name__ == "__main__":
    main()




