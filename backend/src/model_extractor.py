import pathlib
import rasa
import glob
import os

def load_interpreter(model_path):
    """
    This loads the Rasa NLU interpreter. It is able to apply all NLU
    pipeline steps to a text that you provide it. 
    """
    model = rasa.cli.utils.get_validated_path(model_path, "model")
    model_path = rasa.model.get_model(model)
    _, nlu_model = rasa.model.get_model_subdirectories(model_path)
    return rasa.nlu.model.Interpreter.load(nlu_model)

def get_last_model_path(model_folder_path):
    list_of_files = glob.glob(model_folder_path+'*') 
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file