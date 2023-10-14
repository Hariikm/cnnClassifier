from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import Evaluation
from cnnClassifier.components import Training
from cnnClassifier import logging




class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):

        config= ConfigurationManager()
        evaluation_config= config.get_validation_config()
        evaluation= Evaluation(config= evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()