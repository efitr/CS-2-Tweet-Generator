//
//  1histogram.py
//  
//
//  Created by Egon Fiedler on 11/21/17.
//

import random
import sys

class Histogram(dict):

    def __init__(self, source_text):
        self = self.histogram(source_text)




def open_text(source_text):
    with open(source_text) as f:
        return f.read().split()


if __name__ == '__main__':
    print(sys.argv[1])

    text = open_text(sys.argv[1])

    histogram = Histogram(text)

    histogram.unique_words()
