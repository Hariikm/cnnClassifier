import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time

from cnnClassifier.entity import PrepareCallbackConfig


class PrepareCallback:

    def __init__(self, config: PrepareCallbackConfig):
        self.config= config


    @property
    def _create_tb_callback(self):
        timestamp= time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir= os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}"
        )
        return tf.keras.callbacks.TensorBoard(log_dir= tb_running_log_dir)
    
    """ 
        When we use this property decorator, if we are calling this fuction (object) else where we dont actually need to specify the () to call
        it. We can access this object like its a attribute.

    """

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath= str(self.config.checkpoint_model_filepath),
            save_best_only= True)
    
    """ 
        Here the explicit str() has given by me as the original code was not working and it was giving out windows path error, even though
        it was creating our desired directories the problem was only with the error, and looking net and GPT this edit was made

    """
    
    def get_tb_ckpt_callbacks(self):
        return[
            self._create_tb_callback,
            self._create_ckpt_callbacks
        ]