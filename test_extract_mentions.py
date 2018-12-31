"""A3. Tester for the function extract_mentions in tweets.
"""

import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    """Tester for the function extract_mentions in tweets.
    """
    
    def first_let_caps(self):
        """if first letter proceeding @ is caps"""
        
        arg = '@TWEET!et test case'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  
        
        
    def two_ats(self):
        """two @'s"""
        
        arg = '@@twe!et test case'
        actual = tweets.extract_mentions(arg)
        expected = ['twe']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
        
    def mixed_symbols(self):
        """if spec char appears in word"""
        
        arg = '@twe!et test case'
        actual = tweets.extract_mentions(arg)
        expected = ['twe']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
        
    def mixed_caps(self):
        """mixed lettering w/ caps"""
        
        arg = '@tWeEt test case'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
        
        
    def test_no_user(self):
        """nothing follows @"""
        
        arg = '@! tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
        
    def test_mult_conj(self):
        """testing conjoined @'s"""
        
        arg = '#tweet@test @testing#ah case'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'testing']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)     
        
        
    def test_mult(self):
        """multiple @'s"""
        
        arg = '@tweet @TEST @cow case'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'test', 'cow']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    

    def test_empty(self):
        """Empty tweet."""

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        """Non-empty tweet with no mentions."""

        arg = 'tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


if __name__ == '__main__':
    unittest.main(exit=False)
