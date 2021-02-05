import random 
import json 
class QuestionHandler:

    def __init__(self):
        with open("./resources/question_classification.json", "r") as read_file:
            self.question_classification = json.load(read_file)
        
    
    def get_random_question(self,category):
        question_category = random.choices(self.question_classification[category])[0]
        for q in question_category.values():
            question_id = random.choices(q['values'])[0]['id']
        return question_id

    def verify_answer(self,question_id,intent):
        answer = self._get_answer_by_id(question_id)
        if intent == answer:
            return True 
        else:
            return False
    
    def get_question_by_id(self,question_id):
        if question_id == None:
            return None
        result = ""
        for question_list in self.question_classification.values():
            for question in question_list[0].values():
                base = question['base']
                for option in question['values']:
                    if option['id'] == question_id:
                       result = base + option['option']
                       break
        return result
    
    def _get_answer_by_id(self,question_id):
        if question_id == None:
            return None
        answer = None 
        for question_list in self.question_classification.values():
            for question in question_list[0].values():
                for option in question['values']:
                    if option['id'] == question_id:
                        answer = option['answer']
                        break 
        return answer
    
    def get_explanation_by_id(self,question_id):
        if question_id == None:
            return None
        explanation = None
        for question_list in self.question_classification.values():
            for question in question_list[0].values():
                for option in question['values']:
                    if option['id'] == question_id:
                        explanation = option['explanation']
                        break 
        return explanation
    
    def get_category_by_id(self,question_id):
        if question_id == None:
            return None
        question_category = None
        for category,question_list in self.question_classification.items():
            question_category = category
            for question in question_list[0].values():
                for option in question['values']:
                    if option['id'] == question_id:
                        break
        return question_category

    