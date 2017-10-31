import random

def random_rearragement(lst):
    '''
    Mix the words
    '''
    rand_rearragement = random.randint(0, len(lst)-1)
    for i in range(len(lst)):
        lst[i], lst[rand_rearragement] = lst[rand_rearragement], lst[i]

words = input("Enter words: ").split(" ")
random_rearragement(words)
print(words)




