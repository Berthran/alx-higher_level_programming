#!/usr/bin/python3

def multiple_returns(sentence):
    count_letters = len(sentence)
    
    if count_letters == 0:
        return(count_letters, None)
    else:
        return(count_letters, sentence[0])

if __name__ == "__main__":
    multiple_returns()
