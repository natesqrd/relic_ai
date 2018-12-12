# coding=utf-8
from stanfordcorenlp.corenlp import StanfordCoreNLP

# in string replace ^ with **
""" All language specifications used from Standford NLP is implemented here.
    This system will use the POS tags to identify words like "Derive", "Integrate"
    or sentences like "Find x of (expression)" or "What are the zeros of this equation (equation). """

nlp = StanfordCoreNLP()
poslist = []
derivative = ['derivative', 'd/dx', 'differentiate', 'derive']
integral = ['integral', 'integrate', 'dx', 'anti-derivative', 'area']
find = ['find', 'isolate', 'zero', 'zeros']

poswords = [()]

def getVB(sentence):
    posSentence = nlp.pos_tag(sentence)
    for poslist in posSentence:
        if list[1] == 'VB':
            vb = list[0]


"""
NLP returns POS and NER as list of lists, to find item or pos/ner
set pos/ner = [] then traverse through list to get item and vice versa 
"""
"""

___POS Codes___
CC Coordinating conjunction
CD Cardinal number
DT Determiner
EX Existential there
FW Foreign word
IN Preposition or subordinating conjunction
JJ Adjective
JJR Adjective, comparative
JJS Adjective, superlative
LS List item marker
MD Modal
NN Noun, singular or mass
NNS Noun, plural
NNP Proper noun, singular
NNPS Proper noun, plural
PDT Predeterminer
POS Possessive ending
PRP Personal pronoun
PRP$ Possessive pronoun
RB Adverb
RBR Adverb, comparative
RBS Adverb, superlative
RP Particle
SYM Symbol
TO to
UH Interjection
VB Verb, base form
VBD Verb, past tense
VBG Verb, gerund or present participle
VBN Verb, past participle
VBP Verb, non­3rd person singular present
VBZ Verb, 3rd person singular present
WDT Wh­determiner
WP Wh­pronoun
WP$ Possessive wh­pronoun
WRB Wh­adverb


___MATH Key Words___

[('Derive', 'VB'), ('Integrate', 'VB'), ('=', 'JJ'), ('sin', 'NN'), ('cos', 'NN'), ('tan', 'NN'), ('exp', 'NN'), 
('ln', 'NN'), ('limit', 'NN')]

[('+', 'CC'), ('-', ':'), ('*', 'SYM'), ('/', ':'), ('**', 'SYM'), ('^', 'SYM'), ('log', 'NN'), ('(', '-LRB-'), (')', 
'-RRB-'), ('!', '.'), ('%', 'NN')]

[('Differentiate', 'VB'), ('integral', 'JJ')]

[('derivative', 'NN')]

"""