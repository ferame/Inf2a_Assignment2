# File: statements.py
# Template file for Informatics 2A Assignment 2:
# 'A Natural Language Query System in Python/NLTK'

# John Longley, November 2012
# Revised November 2013 and November 2014 with help from Nikolay Bogoychev
# Revised November 2015 by Toms Bergmanis and Shay Cohen


# PART A: Processing statements
import re
import nltk


def add(lst, item):
    if item not in lst:
        lst.insert(len(lst), item)


class Lexicon:
    """stores known word stems of various part-of-speech categories"""

    def __init__(self):
        self.P = []
        self.N = []
        self.A = []
        self.I = []
        self.T = []

    def add(self, stem, cat):
        if cat == "P":
            self.P.append(stem)
        elif cat == "N":
            self.N.append(stem)
        elif cat == "A":
            self.A.append(stem)
        elif cat == "I":
            self.I.append(stem)
        elif cat == "T":
            self.T.append(stem)

    def getAll(self, cat):
        if cat == "P":
            p = list(set(self.P))
            return p
        elif cat == "N":
            n = list(set(self.N))
            return n
        elif cat == "A":
            a = list(set(self.A))
            return a
        elif cat == "I":
            i = list(set(self.I))
            return i
        elif cat == "T":
            t = list(set(self.T))
            return t


class FactBase:
    # add code here
    def __init__(self):
        self.Unaries = []
        self.Binaries = []

    def addUnary(self, pred, e1):
        self.Unaries.append((pred, e1))

    def addBinary(self, pred, e1, e2):
        self.Binaries.append((pred, e1, e2))

    def queryUnary(self, pred, e1):
        isUnary = False
        for unary in self.Unaries:
            if ((pred, e1) == unary):
                isUnary = True
        return isUnary

    def queryBinary(self, pred, e1, e2):
        isBinary = False
        for binary in self.Binaries:
            if ((pred, e1, e2) == binary):
                isBinary = True
        return isBinary


# from nltk.corpus import brown


def verb_stem(s):
    if verb(VB/VBZ)then continue
    if vb/vbz = have/do then xit
    else exit, not verb
    word = nltk.word_tokenize(s)
    if()

    """extracts the stem from the 3sg form of a verb, or returns empty string"""
    vowel = ['a', 'e', 'i', 'o', 'u']
    stem_length = len(s)

    if re.match("[a-z]+[^(ies|oes|ses|xes|zes|ches|shes)]$", s) and re.match("[a-z]es$", s):
        s = s[:stem_length - 1]
        print("first")
        return s
    # if stem ends with e, with the second to last letter not being i,o,s,x,z,ch,sh add s

    if re.match('has', s):
        s = 'have'
        print("second")
        return s
    # if stem is have, change to has

    if re.match("[a-z]+[^(sses|zzes)]$", s) and re.match("[a-z]+[^(ses|zes)]$", s):
        s = s[:stem_length - 1]
        print("third")
        return s
    # if ends not with sse or zze, but se, ze, add s

    if re.match("[a-z]+[o|x|ch|sh|ss|zz]es$", s):
        s = s[:stem_length - 2]
        print("fourth")
        return s
    # if ends with o,x,ch,sh,ss,zz add es

    if stem_length == 4 and re.match("[a-z]+[^aeiou]ies$", s):
        s = s[:stem_length - 1]
        print("fifth")
        return s
    # if 2 last letters are ie and length == 3 and first letter is nonvowel, then add s

    if stem_length >= 3 and re.match("[a-z]+[^aeiou]ies$", s):
        s = s[:stem_length - 3] + 'y'
        print("sixth")
        return s
    # if ends in nonvowel + y and length >= 3, change y to ies

    if not re.match("[a-z]+[s|x|y|z|ch|sh|a|e|i|o|u]s$", s):
        s = s[:stem_length - 1]
        print("seventh")
        return s
    # if ends not in s,x,y,z,ch,sh or vowel then add s

    if re.match("[a-z]+[a|e|i|o|u]ys$", s):
        s = s[:stem_length - 1]
        print("eighth")
        return s
    # if ends in vowel + y then add s

    return "Empty string"
        # add code here


def add_proper_name(w, lx):
    """adds a name to a lexicon, checking if first letter is uppercase"""
    if ('A' <= w[0] and w[0] <= 'Z'):
        lx.add(w, 'P')
        return ''
    else:
        return (w + " isn't a proper name")


def process_statement(lx, wlist, fb):
    """analyses a statement and updates lexicon and fact base accordingly;
       returns '' if successful, or error message if not."""
    # Grammar for the statement language is:
    #   S  -> P is AR Ns | P is A | P Is | P Ts P
    #   AR -> a | an
    # We parse this in an ad hoc way.
    msg = add_proper_name(wlist[0], lx)
    if (msg == ''):
        if (wlist[1] == 'is'):
            if (wlist[2] in ['a', 'an']):
                lx.add(wlist[3], 'N')
                fb.addUnary('N_' + wlist[3], wlist[0])
            else:
                lx.add(wlist[2], 'A')
                fb.addUnary('A_' + wlist[2], wlist[0])
        else:
            stem = verb_stem(wlist[1])
            if (len(wlist) == 2):
                lx.add(stem, 'I')
                fb.addUnary('I_' + stem, wlist[0])
            else:
                msg = add_proper_name(wlist[2], lx)
                if (msg == ''):
                    lx.add(stem, 'T')
                    fb.addBinary('T_' + stem, wlist[0], wlist[2])
    return msg


# End of PART A.

x = Lexicon()
x.add("John", "P")
x.add("Mary", "P")
x.add("like", "T")
print(x.getAll("P"))

fb = FactBase()
fb.addUnary("duck", "John")
fb.addBinary("love", "John", "Mary")
print(fb.queryUnary("duck", "John"))
print(fb.queryBinary("love", "Mary", "John"))

print(verb_stem("flies"))
print(verb_stem("flys"))
