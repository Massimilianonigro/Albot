import pathlib
from rasa.cli.utils import get_validated_path
from rasa.model import get_model, get_model_subdirectories
from rasa.nlu.model import Interpreter
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.constants import TEXT
import glob
import os

def load_interpreter(model_path):
    """
    This loads the Rasa NLU interpreter. It is able to apply all NLU
    pipeline steps to a text that you provide it. 
    """
    model = get_validated_path(model_path, "model")
    model_path = get_model(model)
    _, nlu_model = get_model_subdirectories(model_path)
    return Interpreter.load(nlu_model)

def get_last_model_path(model_folder_path):
    list_of_files = glob.glob(model_folder_path+'*') 
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file