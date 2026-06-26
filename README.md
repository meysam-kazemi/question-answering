# Question-Answering Transformer Model

## Overview

This repository is a practice project for fine-tuning and running a transformer-based
model for question-answering tasks. The goal is to deepen understanding of transformer
architectures in NLP by building and experimenting with a model on a question-answering
dataset. It includes scripts for training, inference, and dataset loading, all driven by
a simple configuration file (`config/config.ini`) for easy customization.

## Project Structure

```
.
├── config/
│   └── config.ini          # Dataset paths, model name, and training hyperparameters
├── data/
│   ├── raw/                # Place your raw dataset here (JSON/CSV)
│   └── load_data.py        # Helper to load the dataset from the configured path
├── notebooks/
│   └── notebook.ipynb      # Exploratory notebook
├── src/
│   ├── model_and_tokenizer.py  # Loads the model and tokenizer
│   ├── inference.py            # Run inference from the command line
│   └── utils.py               # Config reader and chat helper
├── train.py                # Entry point for training
└── requirements.txt        # Python dependencies
```

## Setup

1. Clone the repository.

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Prepare the dataset:

   - Place your question-answering dataset in `data/raw/`.
   - Update the `path` field in `config/config.ini` if you use a different directory.

### GPU support

The project uses a quantized model (`Qwen2.5-32B-Instruct-GPTQ-Int4`), which requires a
CUDA-compatible GPU for efficient training and inference. Make sure PyTorch is installed
with CUDA support.

## Configuration

All settings live in `config/config.ini`:

| Section       | Key             | Description                              |
| ------------- | --------------- | ---------------------------------------- |
| `[dataset]`   | `path`          | Path to the dataset directory            |
| `[model]`     | `model_name`    | Hugging Face model identifier            |
| `[train]`     | `save_dir`      | Directory for saving checkpoints         |
| `[train]`     | `epoch`         | Number of training epochs                |
| `[train]`     | `learning_rate` | Learning rate                            |
| `[train]`     | `weight_decay`  | Weight decay                             |
| `[inference]` | `best_model`    | Path to the trained model for inference  |

## Usage

### Training

```bash
python train.py
```

The script reads settings from `config/config.ini`, including the dataset path, model
name, and training hyperparameters. Checkpoints are saved to the directory given by
`save_dir`.

### Inference

Point `best_model` in `config/config.ini` to a trained checkpoint, then run:

```bash
python src/inference.py --prompt "Your question here"
```
