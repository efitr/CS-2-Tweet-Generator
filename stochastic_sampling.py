from random import randrange
import sys

class Histogram(dict):
        
    def __init__(self, source_text):
        self = self.histogram(source_text)
        #self.source_text = source_text
        ##self.histogram_dict = {}
    
    def histogram(self, sour_text):
        histo_dict = {}
        #sour_text = self.source_text
        for word in sour_text:
            if word not in histo_dict:
                histo_dict[word] = 1
            else:
                histo_dict[word] += 1
        ##self.histogram_dict = histo_dict
        return histo_dict

    def weighted_frequency_dict(self, histo_dict):
        ##histogram = self.histogram_dict
        for word in histo_dict: 
            histo_dict[word] = histo_dict[word] / len(histo_dict)
        
        return histo_dict

    def rand_word(self, histo_dict):
        """ 
        """
        random_word_index = randrange(0, len(histo_dict))
        #random_word = histo_dict[random_word_index]
        word_list = list(histo_dict.keys())
        random_word = word_list[random_word_index]
        print(random_word)
        return random_word

'''
    def unique_words(self):
        print('hi')
        unique_arr = []
        for key,val in self.items():
            print("The key is {} and val is {}".format(key,val))
        return True
'''

def open_text(source_text):
    with open(source_text) as f:
        return f.read().split()


if __name__ == '__main__':
    print(sys.argv[1])
    # Return the text from open text
    text = open_text(sys.argv[1])
    # pass text into hisogram
    histogram = Histogram(text)
    histogram.histogram(text)
    histogram.weighted_frequency_dict(histogram.histogram(text))
    #source_text = " ".join(ss)
    #histogram.unique_words()
    histogram.rand_word(histogram.histogram(text))