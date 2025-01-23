from transformers import TrainingArguments, Trainer
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.utils import read_config
from src.model_and_tokenizer import modelAndTokenizer
from data.load_data import load_the_dataset
config = read_config()
train_dataset, validation_dataset = load_the_dataset(config)
mt = modelAndTokenizer(config)

args = TrainingArguments(
    config['train']['save_dir'],
    evaluation_strategy="no",
    save_strategy="epoch",
    learning_rate=float(config['train']['learning_rate']),
    num_train_epochs=int(config['train']['epoch']),
    weight_decay=float(config['train']['weight_decay']),
    fp16=True,
    push_to_hub=False,
)


trainer = Trainer(
    model=mt.model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=validation_dataset,
    tokenizer=mt.tokenizer,
)
trainer.train()

