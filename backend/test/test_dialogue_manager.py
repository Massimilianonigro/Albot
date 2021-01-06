import sys
sys.path.insert(0, '../src')

from dialogue_manager import DialogueManager
from model_extractor import load_interpreter
import unittest

model_directory_path = '../NLUmodule/models'

class TestDialogueManager(unittest.TestCase): 

    def setUp(self):
        self.dialogue_manager = DialogueManager(load_interpreter(model_directory_path))

    def test_init(self):
        self.assertNotEqual(self.dialogue_manager.ingredients_list,None)

    def test_add_user(self):
        self.dialogue_manager.add_user(1)
        self.assertEqual(len(self.dialogue_manager.users),1)
        
    def test_del_user(self):
        self.dialogue_manager.add_user(1)
        self.dialogue_manager.del_user(1)
        self.assertEqual(len(self.dialogue_manager.users),0)

    def test_generate_utterance(self):
        self.dialogue_manager.add_user(1)
        test_utterance = self.dialogue_manager.generate_utterance("test",1)
        self.assertEqual(test_utterance,0)

if __name__ == "__main__":
    unittest.main()





