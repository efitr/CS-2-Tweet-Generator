from flask import Flask, request
from markov_model import markov_chain, generate_sentence
from clean_up import clean_file


app = Flask(__name__)

@app.route('/')
def markov_sentence():
    clean_text_list = clean_file('corpus.txt')
    markov_word = markov_chain(clean_text_list)
    sentence = generate_sentence(10, markov_word)
    return sentence

if __name__ == '__main__':
    app.run()
    app.config("DEBUG") == True