from time import time
import math

word_list = ["Mathew", "Ralp", "Harrilal", "Ralph", "Tyler", "Mathew"]

def time_random():
    return (time() - float(str(time()).split('.')[0]))

def gen_random_range(min, max):
    return float(time_random() * (max + min) - min)

