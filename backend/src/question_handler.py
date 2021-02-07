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

    #Returns 0 if the answer is wrong, 1 if the answer is good, 2 if the intent is not meant to answer the question
    def verify_answer(self,question_id,intent):
        answer = self._get_answer_by_id(question_id)
        if (self._is_click_answer(answer) and self._is_click_answer(intent)) or (self._is_text_answer(answer) and self._is_text_answer(intent)):
            #This means answer and intent are either both text or click
            if answer == intent:
                return 1
            elif not self._is_clarification(intent):
                return 0
        else:
            return 2

        
            

    
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
                       return result
        return result
    
    def _is_click_answer(self,answer):
        if answer[0:7] == "clicked":
            return True
        else:
            return False
    
    def _is_text_answer(self,answer):
        return not self._is_click_answer(answer)
    
    def _is_clarification(self,intent):
        if intent[0:6] == "inform":
            return True
        else:
            return False
    
    def _get_answer_by_id(self,question_id):
        if question_id == None:
            return None
        answer = None 
        for question_list in self.question_classification.values():
            for question in question_list[0].values():
                for option in question['values']:
                    if option['id'] == question_id:
                        answer = option['answer']
                        return answer 
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
                        return explanation 
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
                        return question_category
        return question_category

    