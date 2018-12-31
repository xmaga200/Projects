"""A3. Tester for the function common_words in tweets.
"""

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    """Tester for the function common_words in tweets.
    """
    
    def four_word_case(self):
        """if N is 4"""
        
    arg1 = {'hello': 2, 'by': 2, 'hi': 1, 'no': 1, 'jam': 0}
    arg2 = 4
    exp_arg1 = {'hello': 2, 'by': 2, 'hi': 1, 'no': 1}
    act_return = tweets.common_words(arg1, arg2)
    exp_return = None

    msg = "Expected {}, but returned {}".format(exp_return, act_return)
    self.assertEqual(act_return, exp_return, msg)

    msg = ("Expected dictionary to be {}\n, " +
           "but it was\n {}").format(exp_arg1, arg1)
    self.assertEqual(arg1, exp_arg1, msg)
    
    
    def all_equal(self):
        """all equal values diff keys"""
        
    arg1 = {'hello': 2, 'by': 2, 'hi': 2}
    arg2 = 2
    exp_arg1 = {}
    act_return = tweets.common_words(arg1, arg2)
    exp_return = None

    msg = "Expected {}, but returned {}".format(exp_return, act_return)
    self.assertEqual(act_return, exp_return, msg)

    msg = ("Expected dictionary to be {}\n, " +
           "but it was\n {}").format(exp_arg1, arg1)
    self.assertEqual(arg1, exp_arg1, msg)
    
    
    def less_than_limit(self):
        """less than threshold N in dict"""
        
    arg1 = {'hello': 2, 'by': 2, 'hi': 1, 'no': 1}
    arg2 = 5
    exp_arg1 = {'hello': 2, 'by': 2, 'hi': 1, 'no': 1}
    act_return = tweets.common_words(arg1, arg2)
    exp_return = None

    msg = "Expected {}, but returned {}".format(exp_return, act_return)
    self.assertEqual(act_return, exp_return, msg)

    msg = ("Expected dictionary to be {}\n, " +
           "but it was\n {}").format(exp_arg1, arg1)
    self.assertEqual(arg1, exp_arg1, msg)
    
    
    def more_than_limit(self):
        """more than N words in dict"""
        
    arg1 = {'hello': 2, 'by': 2, 'hi': 1, 'no': 1}
    arg2 = 3
    exp_arg1 = {'hello': 2, 'by': 2}
    act_return = tweets.common_words(arg1, arg2)
    exp_return = None

    msg = "Expected {}, but returned {}".format(exp_return, act_return)
    self.assertEqual(act_return, exp_return, msg)

    msg = ("Expected dictionary to be {}\n, " +
           "but it was\n {}").format(exp_arg1, arg1)
    self.assertEqual(arg1, exp_arg1, msg)
        
        
    def less_than_limit(self):
        """all tied"""
        
    arg1 = {'hello': 2, 'by': 2}
    arg2 = 1
    exp_arg1 = {'hello': 2}
    act_return = tweets.common_words(arg1, arg2)
    exp_return = None

    msg = "Expected {}, but returned {}".format(exp_return, act_return)
    self.assertEqual(act_return, exp_return, msg)

    msg = ("Expected dictionary to be {}\n, " +
           "but it was\n {}").format(exp_arg1, arg1)
    self.assertEqual(arg1, exp_arg1, msg)
    
    
    def test_two_word_limit(self):
        """dictionary w/ 2 words"""
        
    arg1 = {'hello': 2, 'by': 2}
    arg2 = 2
    exp_arg1 = {'hello': 2, 'by': 2}
    act_return = tweets.common_words(arg1, arg2)
    exp_return = None

    msg = "Expected {}, but returned {}".format(exp_return, act_return)
    self.assertEqual(act_return, exp_return, msg)

    msg = ("Expected dictionary to be {}\n, " +
           "but it was\n {}").format(exp_arg1, arg1)
    self.assertEqual(arg1, exp_arg1, msg)    
    
    
    def test_empty(self):
        """Empty dictionary."""

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


if __name__ == '__main__':
    unittest.main(exit=False)
