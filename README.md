# Question-Answering Transformer Model
### Overview
This repository contains a practice project for implementing and training a transformer-based model for question-answering tasks. The goal is to deepen understanding of transformer architectures in natural language processing (NLP) by building and experimenting with a model on a question-answering dataset. The project includes code for training the model, evaluating its performance, and performing inference, leveraging a configuration file (config.ini) for easy customization.
Project Structure

data/: Directory for storing the question-answering dataset.
raw/: Raw dataset files (e.g., JSON or CSV format with questions, contexts, and answers).


src/: Source code for the model implementation and scripts.
train.py: Script to train the question-answering model.

config/config.ini: Configuration file specifying dataset paths, model details, and training hyperparameters.
requirements.txt: List of Python dependencies required to run the project.


### Setup

Clone the repository

Install dependencies:
```
pip install -r requirements.txt
```

Prepare the dataset:

Place your question-answering dataset in the data/raw/ directory.
Update the path field in config.ini if using a different directory.


GPU Support:
The project uses a quantized model (Qwen2.5-32B-Instruct-GPTQ-Int4), which requires a CUDA-compatible GPU for efficient training and inference.
Ensure PyTorch with CUDA support is installed.

Usage
Training the Model
To train the question-answering model, run:
```
python train.py
```

The script reads settings from config.ini, including the dataset path, model name, and training hyperparameters.
Trained model checkpoints are saved in the `models/ directory`.

Ensure the best_model field in config.ini points to the trained model checkpoint.
