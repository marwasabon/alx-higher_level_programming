#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)

    if len(sentence) is 0:
        return (0, None)

    return (len(sentence), sentence[0])
