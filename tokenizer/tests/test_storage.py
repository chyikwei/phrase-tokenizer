import random
from unittest import TestCase
from tokenizer.storage import DictTokenStats

class TestDictTokenStats(TestCase):

    def setUp(self):
        self.tokens = {
            'token_1': 1,
            'token_2': 10,
            'token_3': 15,
        }

        token_stats = DictTokenStats()
        token_id = 1
        for token, value in self.tokens.iteritems():
            t_id = token_stats.set_token_stats(token, value)
            self.assertEqual(t_id, token_id)
            token_id += 1    

        self.token_stats = token_stats

    def test_get_token_stats(self):
        token_stats = self.token_stats
        for token, value in self.tokens.iteritems():
            self.assertEqual(token_stats.get_token_stats(token), value)

    def test_get_token_id_find(self):
        token_stats = self.token_stats
        for token, value in self.tokens.iteritems():
            token_id = token_stats.get_token_id(token)
            self.assertTrue(token_id > 0)

    def test_get_token_id_not_found(self):
        token_stats = self.token_stats
        token_id = token_stats.get_token_id("invalid token")
        self.assertEqual(token_id, None)

    def test_increment_token(self):
        token_stats = self.token_stats
        for token, value in self.tokens.iteritems():
            inc_val = random.randint(1,10)
            token_id = token_stats.increment_token(token, inc_val)
            self.assertEqual(token_id, token_stats.get_token_id(token))
            new_value = token_stats.get_token_stats(token)
            self.assertEqual(new_value, value + inc_val)

