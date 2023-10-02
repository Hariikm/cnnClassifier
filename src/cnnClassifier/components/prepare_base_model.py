from pathlib import Path
import tensorflow as tf
from cnnClassifier.entity import (PrepareBaseModelconfig)




class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelconfig):

        self.config = config

    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape = self.config.params_image_size,
            weights= self.config.params_weights,
            include_top= self.config.params_include_top
        )

        self.save_model(path= self.config.base_model_path, model=self.model)   # Save_model defined at last


    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):

        if freeze_all:
            for layer in model.layers:
                model.trainable = False                          # Freezing all the layers

        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)    

        """ 
            We need to do the flattem explicitely becuase we are only taking the convolution part
            of the model with include_top = False, thus it wont have its predetermined fully connected layers
            so we add the flatten layer here 
         
         """

        prediction = tf.keras.layers.Dense(
            units= classes,
            activation= 'softmax'
        )(flatten_in)

        """ 
            Now we created a Dense layer, This is the output layer, here we are not creating any hidden layyers for the learning purpose,
            as the we are using the defualt weights from imagenet, which is a huge dataset, so our model is already trained for indentifying
            various objects using imagenet dataset. So here we are only using the convolutional layer of the VGG16 model as a feature 
            extractor. [ Here even if we retrain, we may not need a lot of computational resources as the weights are already computed ].
            SO we are only using a ouput layer with 2 neurons.

        """


        full_model = tf.keras.models.Model(
            inputs= model.input,
            outputs= prediction
        )

        full_model.compile(
            optimizer= tf.keras.optimizers.SGD(learning_rate= learning_rate),
            loss= tf.keras.losses.CategoricalCrossentropy(),
            metrics= ["accuracy"]
            )
        
        full_model.summary()
        return full_model


    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model= self.model,
            classes= self.config.params_classes,
            learning_rate= self.config.params_learning_rate,
            freeze_all= True,
            freeze_till= None
        )

        self.save_model(path= self.config.updated_base_model_path, model= self.full_model)


    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)