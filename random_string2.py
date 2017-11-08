import random 

choices = ([1,2,3,4], [5,6,7,8,9], [4,6,1,3], [4,5,1,3,2,2]) 

def random_python_numarray():
    rand_index = random.randint(0, len(choices)-1)
    return choices[rand_index]

if __name__ == '__main__':
    choice = random_python_numarray()
    print (choice)
