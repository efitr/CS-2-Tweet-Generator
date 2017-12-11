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
        random_word = current_dictogram.return_weighted_random_word()
        current_word = random_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'
    return sentence

def generate_random_sentence_n(lenght, markov_model):
    current_window = get_start_token(markov_model)
    sentence = [current_window[0]]
    tweet = ''

    valid_tweet_flag = True
    sentence_count = 0
    while valid_tweet_flag:
        current_dictogram = markov_model[current_window]
        random_weighted_word = current_dictogram.return_weighted_random_word()

        current_window_deque = deque(current_window)
        current_window_deque.popleft()
        current_window_deque.append(random_weighted_word)
        current_window = tuple(current_window_deque)
        sentence.append(current_window[0])

        if current_window[1] == 'end' or current_window[1] == '[end]':
            sentence_string = ' '.join(sentence)
            sentence_string = re.sub('end', '. ', sentence_string, flags=re.IGNORECASE)
            sentence_string = sentence_string.capitalize()
            new_tweet_len = len(sentence_string) + len(tweet)

            if sentence_count == 0 and new_tweet_len < lenght:
                tweet += sentence_string
                sentence_string = ' '.join(sentence)
                sentence_count += 1
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            
            elif sentence_count == 0 and new_tweet_len >= lenght:
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            
            elif sentence_count > 0 and new_tweet_len < lenght:
                tweet += sentence_string
                sentence_string = ' '.join(sentence)
                sentence_count += 1
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            
            else:
                return tweet

if __name__ == '__main__':
    clean_text_list = clean_file('')