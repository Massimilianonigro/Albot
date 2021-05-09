from albot_backend.state import State
import json


class StateEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj) is State:
            return {"__enum__": str(obj)}
        return json.JSONEncoder.default(self, obj)


def as_enum(d):
    if "__enum__" in d:
        _, state = d["__enum__"].split(".")
        return State[state]
    else:
        return d


def get_dict(file_path):
    return json.load(open(file_path, "r"), object_hook=as_enum)
