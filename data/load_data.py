"for load the dataset"

import os
import sys
from datasets import load_dataset
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.utils import read_config, red_print


def load_the_dataset(config):
    """
    Load the dataset locally from the path given in the config.
    Assumes the data is in JSON format.
    """
    path = config["dataset"]['path']
    try:
        return load_dataset(path)
    except Exception as error:
        red_print(f'Loading the data failed: {error}')
        return None


# Example usage:
if __name__ == "__main__":
    config = read_config()
    data = load_the_dataset(config)
    print(data)
