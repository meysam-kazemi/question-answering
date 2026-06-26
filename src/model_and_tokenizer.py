"""for load model and tokenizer"""
import os
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.utils import read_config, red_print

class modelAndTokenizer:
    def __init__(self, config, inference=False):
        self.model = None
        self.tokenizer = None
        if inference:
            self.model_name = config['inference']['best_model']
        else:
            self.model_name = config['model']['model_name']

        try:
            self._load_and_model_and_tokenizer()
        except Exception as error:
            red_print(f"Loading model failed: {error}")

    def _load_and_model_and_tokenizer(self):
        """
        Loads a pre-trained model and tokenizer.
        """
        # Load the model and tokenizer
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map="auto"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name
        )

        print(f"\nModel and tokenizer for '{self.model_name}' loaded.")

    
if __name__=="__main__":
    config = read_config()
    mt = modelAndTokenizer(config)