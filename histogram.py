import random
import sys

class Histogram(dict):
        
    def __init__(self, source_text):
        self = self.histogram(source_text)
        #self.source_text = source_text
    
    def histogram(self, sour_text):
        histo_dict = {}
        #sour_text = self.source_text
        for word in sour_text:
            if word not in histo_dict:
                histo_dict[word] = 1
            else:
                histo_dict[word] += 1
        print(histo_dict)
        return histo_dict

    def unique_words(self):
        print('hi')
        unique_arr = []
        for key,val in self.items():
            print("The key is {} and val is {}".format(key,val))
        return True


def open_text(source_text):
    #
    with open(source_text) as f:
        return f.read().split()


if __name__ == '__main__':
    print(sys.argv[1])
    # Return the text from open text
    text = open_text(sys.argv[1])
    # pass text into hisogram
    histogram = Histogram(text)
    #source_text = " ".join(ss)
    histogram.unique_words()

    """
    Feedback:
    - Perhaps use more semantic variable names even tho
    they r a pain to type
    - Maybe move opening of the text in the __init__ function
    """
