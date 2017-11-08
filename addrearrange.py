import random
'''
words = ("how", "now", "brown", "cow")

def random_rearrangement(shuffle_words):
    rand_rearragement = random.randint(0, len(shuffle_words)-1)
    # return words[rand_rearragement]
    shuffle_words[rand_rearragement], shuffle_words[rand_rearragement] = shuffle_words[rand_rearragement], shuffle_words[rand_rearragement]
    return words

if __name__ == '__main__':
    word = random_rearrangement(words)
    print (word)
    print(random_rearrangement(words))
'''
def scrambleList(lst):
    rand_index = random.randint(0, len(lst) - 1)
    for i in range(len(lst)):
        lst[i], lst[rand_index] = lst[rand_index], lst[i]

words = input("Enter words: ").split(" ")
scrambleList(words)
print(words)