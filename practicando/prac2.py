import random 

def random_rearrangement(lst):
    rand_rearrangement = random.randint(0, len(lst)-1)
    for i in range(len(lst)):
        lst[i], lst[rand_rearrangement] = lst[i], lst[rand_rearrangement]

    words = input("Enter words: ").split()
    rand_rearrangement(words)
    print(words)
