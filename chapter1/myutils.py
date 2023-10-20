"""
This module contains utility functions for the project.
"""
import yaml
import os


def api_call_simulator(func):
    """
    decorator to simulate an api call during development to avoid api charges
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs) -> str:
        message = f"Called {func.__name__} \n with args: {args} \n, kwargs: {kwargs} \n"
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return "This is a simulated api sample response. \n" + message

    return wrapper


def read_yaml(template_config_path: str = 'template_config.yaml') -> dict:
    """
    Read yaml file and return a dictionary
    :param template_config_path: str(path to yaml file)
    :return:dict
    """
    with open(template_config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


def read_text_file(file_path: str) -> str:
    """
    Read text file and return a string
    :param file_path: str(path to text file)
    :return:str
    """
    with open(file_path, 'r') as f:
        text = f.read()
    return text


def write_openai_response_to_file(file_path: str, response: str):
    """
    Write openai response to file
    :param file_path: str(path to file)
    :param response: str(response to write to file)
    :return: 1
    """
    # response = response.split("\n")
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(response)
    else:
        with open(file_path, 'a') as f:
            f.write(response)
    return 1
