import os
import urllib.request as request
from zipfile import ZipFile
from tqdm import tqdm
from pathlib import Path

from cnnClassifier.entity import DataIngestionConfig
from cnnClassifier import logging
from cnnClassifier.utils import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logging.info("Trying to download file..")
        if not os.path.exists(self.config.local_data_file):
            logging.info("Download started..")
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )
            logging.info(f"{filename} download! with the following info:\n{headers}")
        else:
            logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
            


    def _get_updated_list_of_files(self, list_of_files):
        return[f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]   # We only take images and not other files like "thumb" or Cat and dog folder
    
    # the lsit of files, will carry the path, and as per the code it checks wheather the path contains .jpg or Cat or Dog ( the folder name ), 
    # Thus it will only get the images from the folder and not from the outside.




    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)                  ## But for this code to function properly we need to create working dir before right? Have we ever created that ?

        if os.path.getsize(target_filepath) == 0:
            logging.info(f"removing file:{target_filepath} of size: {get_size(Path(target_filepath))}")
            os.remove(target_filepath)


    def unzip_and_clean(self):
        logging.info(f"unzipping file and removing unwanted files")
        with ZipFile(file= self.config.local_data_file, mode= "r") as zf:
            list_of_files= zf.namelist()
            updated_list_of_files= self._get_updated_list_of_files(list_of_files)

            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)