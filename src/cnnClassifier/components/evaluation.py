from urllib.parse import urlparse
from cnnClassifier.entity import EvaluationConfig
from pathlib import Path
import tensorflow as tf
from cnnClassifier.utils import save_json

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config= config

    def _valid_generator(self):

        datagenerator_kwargs= dict(
            rescale= 1./255,        # Here we doing the basic rescaling, which is making the images from 0-1
            validation_split= 0.20
        )

        dataflow_kwargs= dict(
            target_size= self.config.params_image_size[:-1],
            batch_size= self.config.params_batch_size,
            interpolation= "bilinear"
        ) 
          # Here when we resize the image to target size, the images will be shrinked
          # therefore new pixels are created and interpolation specify which method
          # should be used to colour the new images, here we use bilinear method
          # which means giving a blende ( averaging ) colur from the nearest pixels

        valid_datagenerator= tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator= valid_datagenerator.flow_from_directory(
            directory= self.config.training_data,
            subset= "validation",
            shuffle= False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model= self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score= self.model.evaluate(self.valid_generator)


        """ 
            Here we also need to mention like

            either, 
                    self.model= self.load_model(self.config.path_of_model)
                    self._valid_generator()
                    self.score= self.model.evaluate(self.valid_generator)

                    -- Here we are assigning the model as a global variable --


            or,

                    model= self.load_model(self.config.path_of_model)
                    self._valid_generator()
                    self.score= model.evaluate(self.valid_generator)

                    -- Here we are assigning the model as a local variable --

            previously,

                    self.model= self.load_model(self.config.path_of_model)
                    self._valid_generator()
                    self.score= model.evaluate(self.valid_generator)

                    -- previously ( st_05 ) we gave it like this, and it worked because we have assighned
                       model= tf.keras.models.load_model("artifacts/training/model.h5")

                       or else it wont work, so it always better to use the first method with self

        """ 

    
    def save_score(self):
        scores= {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path= Path("scores.json"), data=scores)