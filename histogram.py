import random
import sys



def histogram(source_text):
    histogram = {}
    for word in source_text:
        if word not in histogram:
            histogram[word] = 0
        histogram[word] += 1
    return histogram

def unique_words(histogram):
    print('hi')
    unique_arr = []
    for key,val in items():
        print("The key is {} and val is {}".format(key,val))
    return True    


if __name__ == '__main__':

    source= ['one','fish','two', 'fish','red', 'fish','blue','fish']
    histo= histogram(source)
    print(histo)
    #histo= unique_words(histo)
    """
    Feedback:
    - Perhaps use more semantic variable names even tho
    they r a pain to type
    - Maybe move opening of the text in the __init__ function
    """
