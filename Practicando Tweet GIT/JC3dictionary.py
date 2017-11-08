import os
import sys
import random
import time

def get_words_list():
    start_time = time.time()
    with open("/usr/share/dict/words", 'r') as directory:
        file_content = directory.read()
    string_list = file_content.split("\n")
    return string_list

num = 10

def randomize(num, string_list):
#''' version 1 '''
    #random_words = [random.choice(string_list) for i in range(num)]
#''' version 2 '''
#    random_words = []
#    for i in range(num):
        random_words.append(random.choice(string_list))
#''' version 3 '''
#    random_sentence = ' '.join(random_words)

    elapsed_time = time.time() - start_time
    print(random_sentence)
    return random_sentence

def main():
    string_list = get_words_list()
    randomize(num, string_list)

main() 
