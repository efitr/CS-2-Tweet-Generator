import random
import sys



def histogram(source_text):
    ''' Create a dictionary, loop through every word in source_text
    and if the word is not in the histogram adds it with a value of
    0 but if it is add a + 1 count to the already there word '''
    histogram = {}
    for word in source_text:
        if word not in histogram:
            histogram[word] = 0
        histogram[word] += 1
    return histogram

def unique_words(histogram):
    '''  '''
    print('hi')
    unique_word = []
    for key,value in items():
        print("The key is {} and value is {}".format(key,value))
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
