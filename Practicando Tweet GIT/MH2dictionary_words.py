import random
import time

with open("/usr/share/dict/words") as word_file:
    read_file = word_file.read()
    split_file = read_file.split()

word_dictionary = {'joyful': 'happy', 'deception': 'sad', 'caca': 'shit'}

amount_of_times = int(input())
def random_sentence(split_file):
    sentence_array = []
    for _ in range(amount_of_times):
        random_index = random.randint(0, len(split_file) - 1)
        sentence_array.append(split_file[random_index])
    return ' '.join(sentence_array)

dictionary_keys = word_dictionary.keys()
random_key = random.choice(list(dictionary_keys))
random_key_index = list(word_dictionary.keys()).index(random_key)

def generate_flash_card(word_dictionary):
    print("Try guessing the definition of the word %s" %(random_key))
    definition_input = str(input())
    if definition_input is not None:
        print("The accurate definition of the word is %s" %(word_dictionary[random_key]))
    return ''

if __name__ == '__main__':
    start_time = time.time()
    print(random_sentence(split_file))
    end_time = time.time()
    print(end_time = start_time)