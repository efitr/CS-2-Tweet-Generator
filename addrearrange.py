import random

''' Power of the program '''
def scrambleList(lst):
    rand_index = random.randint(0, len(lst) - 1)
    print(lst)
    for i in range(len(lst)):
        lst[i], lst[rand_index] = lst[rand_index], lst[i]
        print(lst)
    print(lst)
''' The program '''
words = input("Enter words: ").split(" ")
scrambleList(words)
print(words)
