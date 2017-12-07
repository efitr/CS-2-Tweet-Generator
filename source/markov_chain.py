from dictogram import Dictogram
import stochastic_sampling 
from random import randint

def dictogram_mark(source_text):

    data = source_text

    data = data.split()

    dictogram = {}

    for position in range(len(data)-1):
        word = data[position]
        next_word = data[position+1]

        if word in dictogram:
            dictogram[word].add_count(next_word)
        else:
            dictogram[word] = Dictogram([next_word])
    return(dictogram)

def markov_sample(dictogram):
    return stochastic_sampling.weighted_sampling(dictogram)

def Markov_chain(dictogram):
    output=['red']
    for word_pos in range(10):
        next_word = markov_sample(dictogram[output[word_pos]])
        output.append(next_word)
    return ' '. join(output)

if __name__=="__main__":
    source = 'one fish two fish red fish blue fish'

    dicto = dictogram_mark(source)  
    print(dicto)

    print(Markov_chain(dicto))


        