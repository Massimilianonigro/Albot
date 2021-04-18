import random as rand
import json

RESOURCES_PATH = "./resources"


class InformHandler:
    def __init__(self):
        self.inform_classification = self.utterances = json.load(
            open(RESOURCES_PATH + "/inform_classification.json", "r")
        )

    def grant_information(self, intent):
        intent_dict = self._get_intent_dict(intent)
        explanation = None
        if intent_dict != None:
            # Search first for the more detailed explanation then for the less ones, first search for the entity name explanation
            if len(intent["entities"]) > 0:
                explanation = self._get_entity_explanation(
                    intent_dict, "entity_name", intent["entities"][0]["value"]
                )
                if explanation == None:
                    explanation = self._get_entity_explanation(
                        intent_dict,
                        "entity_group",
                        intent["entities"][0]["entity"]
                        .replace('"', "")
                        .replace("\\", ""),
                    )
            if explanation == None:
                explanation = self._get_general_explanation(intent_dict)
            return explanation
        return explanation

    # Returns entity name or group explanation, matching it with the inserted value[entity key can be either "entity_name" or "entity_group"]
    def _get_entity_explanation(self, intent_dict, entity_key, entity_value):
        for explanation in intent_dict:
            if entity_key in explanation.keys():
                if entity_value.lower() in explanation[entity_key].lower():
                    return explanation["explanation"]
        return None

    # Searches for the object with one key, the explanation one. And the explanation
    def _get_general_explanation(self, intent_dict):
        print(intent_dict)
        for explanation in intent_dict:
            if len(explanation.keys()) == 1:
                if "explanation" in explanation.keys():
                    return explanation["explanation"]
                else:
                    raise Exception("Key explanation is not in inform object")
        raise Exception("General explanation not found in inform object")

    def _get_intent_dict(self, intent):
        if intent["intent"]["name"] in self.inform_classification.keys():
            return self.inform_classification[intent["intent"]["name"]]
        else:
            return None
