from dictogram import Dictogram
from random import randint
import re
from clean_up import clean_file
from collections import deque

def markov_chain(source):
    markov_chain = dict()
    for index in range(0, len(source)-1):
        if source[index] in markov_chain:
            markov_chain[source[index]].update([source[index+1]])
        else:
            markov_chain[source[index]].update([source[index+1]])
    return markov_chain

def any_order_markov_model(order,source):
    markov_model = dict()

    for i in range(0, len(source)-order):
        window = tuple(source[i: i+order])
        if window in markov_model:
            markov_model[window].update([source[i+order]])
        else:
            markov_model[window] = Dictogram([source[i+order]])
    return markov_model

if __name__ == '__main__':
    clean_text_list = clean_file('The Karamazov Brothers.rtf')
    #print(clean_text_list)
    markov_chaining = any_order_markov_model(2,clean_text_list)