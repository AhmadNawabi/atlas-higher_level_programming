#!/usr/bin/python3

def multiple_returns(sentence):

    # Check if the sentence is empty
    if len(sentence) == 0:
        return (0, None)# Return a tuple with length 0 and None as the first character
    else:
        return (len(sentence), sentence[0])# Return a tuple with length of the sentence and its first character
