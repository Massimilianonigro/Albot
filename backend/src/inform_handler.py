import random 
import json 
class InformHandler:

    def __init__():
        with open("./resources/ingredients_list.json", "r") as read_file:
            self.ingredients_list = json.load(read_file)
        with open("./resources/utterances.json", "r") as read_file:
            self.utterances = json.load(read_file)
    
    def grant_information(self,intent):
        explanation = self.options[intent['intent']['name']](self,intent)
        return explanation
    
    def inform_ph(self,intent):
       return rand.choices(self.utterances['ph_explanation'])[0]
    
    def inform_ph_property(self,intent):
        if intent['entities'][0]["value"][0:4] == 'base':
                return rand.choices(self.utterances['base_explanation'])[0]
            elif intent['entities'][0]["value"][0:4] == 'acid':
                return rand.choices(self.utterances['acid_explanation'])[0]
            else:
                return "Did not understand the ph entity you want info about"
    
    def inform_cabbage_solution(self,intent):
       return rand.choices(self.utterances['cabbage_solution_explanation'])[0]
    
    def inform_ingredient_property(self,intent):
        ingredient = self._get_ingredient_used(intent) 
        if ingredient == None:
            return "Ingredient not recognized"
        ingredient_ph = self._get_ingredient_ph(ingredient)
        explanation = "The " + ingredient + " has a ph of " + str(ingredient_ph)
        if ingredient_ph == 7:
            explanation = explanation + " and is thus a neutral substance. " +  rand.choices(self.utterances['properties_neutral_ingredient'])[0]
        elif ingredient_ph < 7:
            explanation = explanation + " and is thus an acid substance. " +  rand.choices(self.utterances['properties_acid_ingredient'])[0]
        elif ingredient_ph > 7:
            explanation = explanation + " and is thus a basic substance. " +  rand.choices(self.utterances['properties_base_ingredient'])[0]
        return explanation
    
    
    #Returns -1 if the ingredient is not in list the ph otherwise
    def _get_ingredient_ph(self,ingredient_used):
        ingredient = ingredient_used.replace(" ", "")
        ingredient = ingredient.lower()
        ingredient_ph = -1
        for i in self.ingredients_list:
            name_in_list = i['name'].replace(" ", "")
            name_in_list = name_in_list.lower() 
            if name_in_list == ingredient:
                ingredient_ph = i['ph']
        return ingredient_ph
        
    def inform_color_change(self,intent):
        color = self._get_color_used(intent)
        ingredient = self._get_ingredient_used(intent)
        elif color != None and ingredient != None:
            #NLU recognized both the ingredient and the color
            ph = self._get_ingredient_ph(ingredient)
            #TODO: Add filtering on color if needed
            if ph == 7:
                return ingredient + " did not change the color of the solution because it is neutral"
            elif ph > 7:
                return ingredient + " is a base hence it changed the color of the solution in " + color
            elif ph < 7:
                return ingredient + " is an acid hence it changed the color of the solution in " + color
        elif color != None and ingredient == None:
            return "The solution became " + color + " due to the ph nature of the ingredient used"
        elif color == None and ingredient != None:
            if ph == 7:
                return ingredient + " did not change the color of the solution because it is neutral"
            elif ph > 7:
                return ingredient + " is a base hence it changed the color of the solution in this way" 
            elif ph < 7:
                return ingredient + " is an acid hence it changed the color of the solution in this way" 
        return rand.choices(self.utterances['cabbage_solution_explanation'])[0]
    
    #Returns None if no color is found, the color otherwise
    def _get_color_used(self,intent):
        if len(intent['entities']) == 0:
            return None
        color = None
        for entity in intent['entities']:
            if "color" in entity['entity']:
                color = entity['value']
        return color

    def _get_ingredient_used(self,intent):
       if len(intent['entities']) == 0:
            return None
        ingredient = None
        for entity in intent['entities']:
            if "ingredient" in entity['entity']:
                ingredient = entity['value']
        return ingredient
    
    options = {
            'inform_ph': inform_ph,
            'inform_ph_property': inform_ph_property,
            'inform_cabbage_solution':inform_cabbage_solution,
            'inform_color_change': inform_color_change,
            'inform_ingredient_property': inform_ingredient_property,
        }