from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils import decodeImage
from cnnClassifier.pipeline.predict import DogCat


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


""" 
    Here we are initialising the language environment as english, ( if we got a search bar, or any other chat bots and stuff like that )
    we might have some inputs for our application hwich should be processed by the programme. So we are basically saying the programme,
    that our language is english and if we type in gift ( which means gift in english and poison in german) we are signifying
    Gift ( in enlgish ) and not tthe poison.

    The LC_ALL says that every other locale variables like LC_MONETARY ( $, € ) we are using $ as the currency sign and not the euro as
    we are using en_US) , LC_COLLATE ( punctuations ), LC_TIME ( Time formats ) in english and not as other languages.

"""

app= Flask(__name__)
CORS(app)

"""
    Here, CORS is used to give multi website request sharing, By default browsers dont allow any websites to make or recieve requests
    from any other websites. But here we need our cliet side ( browser ) [ frontend ] {index.html} to make requests to our 
    backend ( app.py ). So we make this as CORS [ Cross-Origin Resource Sharing ]

"""


class ClientApp:

    def __init__(self):
        self.filename= "inputImage.jpg"
        self.classifier= DogCat(self.filename)

@app.route("/", methods= ['GET'])
@cross_origin()
def home():
    return render_template('index.html')


"""
     Basically we use GET for getting server output and its less secure than the POST as its visible in the URL. But POST is 
     more secure and is basically used for input purposes.

"""


@app.route("/train", methods= ['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully"

"""
    @cross_origin() is same as CORS, by giving CORS(app) we made this global so we dont necessarily want 
    to mention @cross_origin() explicitely for every methods.

"""


@app.route("/predict", methods= ['POST'])
@cross_origin()
def predictRoute():
    image= request.json['image']
    decodeImage(image, clApp.filename)
    result= clApp.classifier.predictiondogcat()
    return jsonify(result)



if __name__ == '__main__':
    clApp= ClientApp()
    app.run(host='0.0.0.0', port=8080)

    """
        Here, the host number 0.0.0.0 means within the network anyone can access this using the port number
    
    """