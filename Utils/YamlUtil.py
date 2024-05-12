import os

import yaml
from dotenv import load_dotenv, find_dotenv

from Config.settings import CONFIG_PATH


def get_config():
    load_env = load_dotenv(find_dotenv(), override=True)
    if load_env is None:
        raise ModuleNotFoundError('.env file not found')
    else:
        current_env = os.getenv('ENV')
        file_path = os.path.join(CONFIG_PATH, current_env+'.yaml')
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)


config_item = get_config()

if __name__ == '__main__':
    print(config_item)

