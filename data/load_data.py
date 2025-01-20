"for load the dataset"

import os
import sys
from datasets import load_dataset
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.utils import read_config, red_print

dataset = load_dataset('data/raw/')

print(dataset)

def load_the_dataset(config):
    """
    for load dataset locally
    Let’s assume the data is in JSON format.
    """
    path = config["dataset"]['path']
    try:
        return load_dataset(path)
    except:
        red_print('Loading the data Failed!!')
        return False
    

# Example usage:
if __name__ == "__main__":
    config = read_config()
    data = load_the_dataset(config)
    print(data)
