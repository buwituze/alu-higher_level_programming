#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (0, None)  # Return a tuple with length 0 and first character as None
    else:
        return (len(sentence), sentence[0])  # Return a tuple with length and first character
