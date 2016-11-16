############################################################
# CIS 521: Homework 7
############################################################

student_name = "Xin Zhang"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import string
import re
import math
############################################################
# Section 1: Markov Models
############################################################
#strig -> [string, string...]
def tokenize(string):
    return re.findall(r"[\w]+|[^\s\w]", string)
    pass

def ngrams(n, tokens):
    result = []
    if n == 1:
        result =  [((),(ele)) for ele in tokens]
        result.append(((),'<END>'))
        return result
    else:
        for i in xrange(len(tokens)):
            token = tokens[i]
            context = []
            for j in xrange(n-1,0,-1):
                if i - j >= 0:
                    context.append(tokens[i - j])
                else:
                    context.append('<START>')
            result.append((tuple(context),token))

        last = tokens[-(n-1):]
        context = [ele for ele in last]
        result.append((tuple(context),'<END>'))
        return result
    pass

class NgramModel(object):

    def __init__(self, n):
        self.n = n
        self.part = {}
        self.total= {}
        pass

    def update(self, sentence):
        ngram = ngrams(self.n,tokenize(sentence))

        for c, t in ngram:
            if c in self.part:
                self.total[c] += 1.0

                if t in self.part[c]:
                    self.part[c][t] += 1.0
                else:
                    self.part[c][t] = 1.0
            else:
                self.total[c] = 1.0
                self.part[c] = {t:1.0}
        pass

    def prob(self, context, token):
        if token in self.part[context]:
            return ( self.part[context][token] / self.total[context])
        else:
            return 0.0
        pass
    

    def random_token(self, context):
        pass

    def random_text(self, token_count):
        pass

    def perplexity(self, sentence):
        pass

def create_ngram_model(n, path):
    pass

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

####test####>>>
m = NgramModel(1)
m.update("a b c d")
m.update("a b a b")
