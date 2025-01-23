import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.model_and_tokenizer import modelAndTokenizer
from src.utils import read_config, red_print, chatQwen

class inference:
    def __init__(self, model, tokenizer):
        self.chat = chatQwen(model, tokenizer)

    def __call__(self, prompt):
        res = self.chat(prompt)
        return res

if __name__=="__main__":
    config = read_config()
    mt = modelAndTokenizer(config, True)
    infer = inference(mt.model, mt.tokenizer)
    prompt = ""
    print(infer(prompt))
    