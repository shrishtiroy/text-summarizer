import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from box import ConfigBox
from pathlib import Path
from typing import List, Union

def read_yaml(file_path: Path) -> ConfigBox:
    """
    Reads a YAML file and returns the contents as a ConfigBox object.

    Args:
        file_path (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        BoxValueError: If the YAML file contains invalid data.

    Returns:
        ConfigBox: A ConfigBox object containing the YAML data.
    """
    try:
        with open(file_path, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {file_path} loaded successfully.")
            if not content:
                raise ValueError("YAML file is empty")
            return ConfigBox(content)
    except BoxValueError as e:
        raise BoxValueError(f"Error in parsing YAML file: {file_path}") from e
    except Exception as e:
        raise e
    
def create_directories(path_to_dir: List[Path], verbose: bool = True) -> None:
    """
    Creates directories if they do not exist.

    Args:
        path_to_dir (List[Path]): List of directory paths to create.
        verbose (bool, optional): If True, shows logging messages. Defaults to True.
    """
    for path in path_to_dir:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory: {path}")

def get_size(file_path: Path) -> str:
    """
    Returns the size of a file in KB.

    Args:
        file_path (Path): The path to the file.

    Returns:
        str: The size of the file in KB.
    """
    size_kb = round(os.path.getsize(file_path)/1024)
    return f"{size_kb} KB"