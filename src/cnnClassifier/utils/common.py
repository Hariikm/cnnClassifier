import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logging
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import joblib 


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yamlfile is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded succesfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs (path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")

            """ Here verbose is True by defualt, So the if condition is like, if verbose is true print the log info, else no """


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path to file

    Returns:
    
        str: size in KB    
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"  # The defualt output is in bytes, we doing /1024 to make that into KBs



@ensure_annotations
def save_json(path: Path, data:dict):

    """ save json data
    
    Args:
    path (Path): path to json file
    data (dict): data to be saved in json file

    """

    with open(path, "w") as f:
        json.dump(data, f, indent= 4)

    logging.info(f"json saved at {path}")



@ensure_annotations
def load_json(path: Path) -> ConfigBox:

    """ load json data
    
    Args:
    path (Path): path to json file

    """

    with open(path) as f:
        content= json.load(f)

    logging.info(f"json loaded successfully from {path}")
    return ConfigBox(content)



@ ensure_annotations
def save_bins(data: Any, path: Path):

    """ Save binary files
    
    Args:

    data : Data to be saved as binary
    path : path to the binary file

    """

    joblib.dump(value= data, filename= path)
    logging.info(f"binary file saved at path {path}")


@ensure_annotations
def load_bins(path: Path) -> Any:

    """Loading binary data
    
    Args:
        path : Path to the binary file

    Returns:
        Any: Object stored in the data
    """

    data= joblib.load(path)
    logging.info(f"binary file loaded from path {path}")
    return data