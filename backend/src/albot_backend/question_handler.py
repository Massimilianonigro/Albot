import random
import json

RESOURCES_PATH = "./resources"

""" [summary] Handles the questions from the bot to the user and the users' answers evaluating their correctness.
"""


class QuestionHandler:
    def __init__(self):
        self.question_classification = json.load(
            open(RESOURCES_PATH + "/question_classification.json", "r")
        )

    def get_random_question(self, category):
        question_category = random.choice(
            self.question_classification[category]["questions"]
        )
        print(question_category)
        return random.choice(list(question_category.values())[0]["values"])["id"]

    # Returns 0 if the answer is wrong, 1 if the answer is good, 2 if the intent is not meant to answer the question
    def verify_answer(self, question_id, intent):
        answer = self._get_answer_by_id(question_id)
        if (self._is_click_answer(answer) and self._is_click_answer(intent)) or (
            self._is_text_answer(answer) and self._is_text_answer(intent)
        ):
            # This means answer and intent are either both text or click
            if answer == intent:
                return 1
            elif not self._is_clarification(intent):
                return 0
        else:
            return 2

    def get_response(self, question_id, positive):
        response = []
        new_pending_question = question_id
        question_type = self._get_question_type_by_id(question_id)
        if question_type == None:
            raise Exception("Question not in the question classification")
        if question_type in self.question_classification.keys():
            if positive:
                response = (
                    response
                    + self.question_classification[question_type]["positive_responses"]
                )
            else:
                response = (
                    response
                    + self.question_classification[question_type]["negative_responses"]
                )
                if self.question_classification[question_type]["explanation"]:
                    response.append(self.get_explanation_by_id(question_id))
            if "more_info" not in self.question_classification[question_type].keys():
                new_pending_question = None
                print("Setting pending_question in get_response(question handler)")
        return new_pending_question, response

    def _get_question_type_by_id(self, question_id):
        if question_id == None:
            return None
        question_type = None
        for (
            classification,
            question_list_category,
        ) in self.question_classification.items():
            question_type = classification
            for question_list_type in question_list_category["questions"]:
                for question in question_list_type.values():
                    for option in question["values"]:
                        if option["id"] == question_id:
                            return question_type
        return question_type

    def get_question_by_id(self, question_id):
        if question_id == None:
            return None
        result = ""
        for question_list_category in self.question_classification.values():
            for question_list_type in question_list_category["questions"]:
                for question in question_list_type.values():
                    base = question["base"]
                    for option in question["values"]:
                        if option["id"] == question_id:
                            result = base + option["option"]
                            return result
        return result

    def _is_click_answer(self, answer):
        if answer[0:7] == "clicked":
            return True
        else:
            return False

    def _is_text_answer(self, answer):
        return not self._is_click_answer(answer)

    def _is_clarification(self, intent):
        if intent[0:6] == "inform":
            return True
        else:
            return False

    def _get_answer_by_id(self, question_id):
        if question_id == None:
            return None
        answer = None
        for question_list_category in self.question_classification.values():
            for question_list_type in question_list_category["questions"]:
                for question in question_list_type.values():
                    for option in question["values"]:
                        if option["id"] == question_id:
                            answer = option["answer"]
                            return answer
        return answer

    def get_explanation_by_id(self, question_id):
        if question_id == None:
            return None
        return "explanation_" + str(question_id)

    def get_category_by_id(self, question_id):
        if question_id == None:
            return None
        question_category = None
        for category, question_list_category in self.question_classification.items():
            question_category = category
            for question_list_type in question_list_category["questions"]:
                for question in question_list_type.values():
                    for option in question["values"]:
                        if option["id"] == question_id:
                            return question_category
        return question_category

    def get_first_id_from_question_name(self, question_name):
        for question_classification_values in self.question_classification.values():
            for question in question_classification_values["questions"]:
                for question_name_key, question_value in question.items():
                    if question_name_key == question_name:
                        return question_value["id"]
        return None
