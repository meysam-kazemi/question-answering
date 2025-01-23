import os
import configparser

def read_config(config_file='config/config.ini'):
    """
    Reads the configuration file and returns the settings as a dictionary.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        dict: A dictionary containing the configuration settings.
    """
    config = configparser.ConfigParser()
    
    # Check if the config file exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"The configuration file '{config_file}' does not exist.")
    
    config.read(config_file)
    
    # Convert config sections to a dictionary
    config_dict = {section: dict(config.items(section)) for section in config.sections()}
    
    return config_dict

def red_print(text):
    """
    Print the given text in red color.

    Args:
        text (str): The text to print in red.
    """
    # ANSI escape code for red text
    RED = "\033[91m\n"
    RESET = "\033[0m\n"  # Reset to default color
    print(f"{RED}{text}{RESET}")


class chatQwen:
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer
        prompt = "I want to improve the prompt. \
            so just improve it and write the improved prompt."
        self.messages = [
            {"role": "system", "content": ""},
        ]

        self.__call__(prompt)

    def __call__(self, prompt):
        self.messages.append(
            {"role": "user", "content": prompt}
        )
        text = self.tokenizer.apply_chat_template(
            self.messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=64
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        self.messages.append(
            {'role':'system', 'content': response}
        )
        return response