from homework7 import *
import unittest
import string

class TestHomework(unittest.TestCase):

    def testTokenize(self):
        string = "  This is an example.  "
        self.assertEqual(tokenize(string),['This', 'is', 'an', 'example', '.'])

        string = "'Medium-rare,' she said."
        self.assertEqual(tokenize(string),["'", 'Medium', '-', 'rare', ',', "'",'she', 'said', '.'])

        

    def testNgrams(self):
        result = [((), 'a'), ((), 'b'), ((), 'c'),((), '<END>')]
        check = ngrams(1, ["a", "b", "c"])
        self.assertEqual(check,result)

        result = [(('<START>',), 'a'), (('a',), 'b'),(('b',), 'c'), (('c',), '<END>')]
        check = ngrams(2, ["a", "b", "c"])
        self.assertEqual(check,result)

        result = [(('<START>', '<START>'), 'a'),(('<START>', 'a'), 'b'),(('a', 'b'), 'c'),(('b', 'c'), '<END>')]
        check = ngrams(3, ["a", "b", "c"])
        self.assertEqual(check,result)

        result = [(('<START>',),'the'),(('the',), 'cow'),(('cow',), 'jumps'),(('jumps',), 'over'),(('over',), 'the'),(('the',), 'moon'),(('moon',),'<END>')]
        check = ngrams(2, ['the','cow' ,'jumps' ,'over' ,'the' ,'moon'])
        self.assertEqual(check,result)

    def testNgramModel(self):
        m = NgramModel(1)
        m.update("a b c d")
        m.update("a b a b")
        result = 0.3
        check = m.prob((), "a")
        self.assertEqual(check,result)
        

        

        
        
                
        

        

unittest.main()
