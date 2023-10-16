import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class DogCat:
    def __init__(self, filename):
        self.filename= filename

    def predictiondogcat(self):
        model= load_model(os.path.join("artifacts","training", "model.h5"))

        imagename= self.filename
        test_image= image.load_img(imagename, target_size= (224,224))
        test_image= image.img_to_array(test_image)
        test_image= np.expand_dims(test_image, axis= 0)     # here the dimension will become ( 1,224,224,3 ) the 1 is the batch size
        result= np.argmax(model.predict(test_image), axis=1)
        # Here the axis signifies per row, ie, the output will be like [.8,.2] here axis= 1 each row is each category, so the argmax will give 0 signifying 0th index got hte max value.
        print(result)

        if result[0] == 1:
            prediction = 'Dog'
            return [{ "image": prediction}]   # In the kaggle dataset its mentioned 1 is dog and 0 is cat
        else:
            prediction= 'Cat'
            return [{ "image": prediction}]