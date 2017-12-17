import sys
import re

def clean_file(source_text):
    source_file = open(source_text, 'r')
    word_list = source_file.read().lower()
    remove_punctuation(word_list)
    result_list = []

    matches = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", word_list)
    for match in matches:
        result_list.append(match)
    return result_list

def remove_punctuation(text):
    no_punctuation_text = re.sub('[,.()]', '', text)
    no_punctuation_text = re.sub('--', ' ', no_punctuation_text)
    no_punctuation_text = re.sub(':', ' ', no_punctuation_text)
    return no_punctuation_text

def main():
    user_argument_count = len(sys.argv)
    if user_argument_count == 1:
        print('Error: textfile not provided')
    else:
        source_file = open(sys.argv[1], 'r')
        word_list = source_file.read().lower()

        matches = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", word_list)
        for match in matches:
            print(match)