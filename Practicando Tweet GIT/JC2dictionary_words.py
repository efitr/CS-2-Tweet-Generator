import os
import sys
import random
import re

with open("/usr/share/dict/words", "r") as directory:
    file_content = directory.read()

num = 5

def randomize(num):
    string_list = list(file_content)

randomize(num)