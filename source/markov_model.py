from dictogram import Dictogram
import stochastic_sampling 
from random import randint

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

def generate_random_start(model):
    if 'END' in model:
        end_word = 'END'
        while end_word == 'END':
            end_word = model['END'].return_weighted_random_word()
        return end_word
    return random.choice(list(model.keys()))
    pass

def get_start_token(markov):
    first_word = random.choice(list(markov.keys()))
    return first_word

def generate_sentence(lenght, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    for i in range(0, lenght):
        current_dictogram = markov_model[current_word]

