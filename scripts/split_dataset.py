#!/usr/bin/env python
"""
Creates an 80 / 20 train-val split of Penn-Fudan Pedestrian.

• Copies each PNG + matching TXT file
  into data/processed/train/… or …/val/…
• Uses a fixed seed for reproducibility.
"""

from pathlib import Path
import random, shutil

ROOT        = Path("data/raw/PennFudanPed")
IMG_SRC     = ROOT / "PNGImages"
ANN_SRC     = ROOT / "Annotation"
TRAIN_DST   = Path("data/processed/train")
VAL_DST     = Path("data/processed/val")

def copy_pair(img, dst_root):
    txt = ANN_SRC / f"{img.stem}.txt"
    (dst_root / "images").mkdir(parents=True, exist_ok=True)
    (dst_root / "ann").mkdir(parents=True, exist_ok=True)
    shutil.copy(img, dst_root / "images" / img.name)
    shutil.copy(txt, dst_root / "ann" / txt.name)

def main(seed=42, ratio=0.8):
    imgs = sorted(IMG_SRC.glob("*.png"))
    random.Random(seed).shuffle(imgs)
    split = int(len(imgs) * ratio)
    train, val = imgs[:split], imgs[split:]

    for p in train: copy_pair(p, TRAIN_DST)
    for p in val:   copy_pair(p, VAL_DST)

    print(f"train {len(train)}  val {len(val)}")

if __name__ == "__main__":
    main()
