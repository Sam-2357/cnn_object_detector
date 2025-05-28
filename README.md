# CNN Object-Detector – Learning Project

*A minimal end-to-end pipeline for understanding how object detectors work.*
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
---

## 🌟 Goals
- Build and train a **tiny CNN** that predicts a single bounding box + class.
- Practise **clean Python project structure**, Git workflow, and code quality tools (`black`, `ruff`, `pytest`).
- Serve as a stepping-stone toward modern detectors (YOLO, Faster R-CNN, etc.).

## 📁 Project Layout (TL;DR)
```text
src/cnn_object_detector/   # package with data, models, engine, utils
notebooks/                 # interactive exploration & tutorials
tests/                     # pytest unit tests
configs/                   # YAML config files (hyper-params)
models/                    # trained checkpoints + logs
data/                      # local copies of datasets
```

## 🚀 Quick start

> **Prerequisites:** Python 3.10+, Git, and a working CUDA install if you want GPU.

```bash
git clone https://github.com/<YOUR-USER>/cnn_object_detector.git
cd cnn_object_detector

# Set up isolated environment
python -m venv .venv
source .venv/bin/activate      # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Lint, format, and test
black .
ruff check .
pytest -q

# training
python -m cnn_object_detector.engine.train \
  --config configs/train_config.yaml
# Results (loss curves, metrics) will appear in models/logs/.
```