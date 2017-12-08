import random
import sys
import histogram


def weighted_sampling(histogram):
    token_count = 0
    for word, freq in histogram.items():
        token_count += freq
    
    randval = random.randint(0, token_count -1)

    for k, v in histogram.items():
        frequency = v

        while frequency > 0:
            if randval > 0:
                randval -= 1
                frequency -= 1
            else:
                return k

if __name__ == '__main__':
    source = ['one', 'fish','two', 'fish', 'blue', 'fish', 'red', 'fish']

    k = weighted_sampling(source)
    print(k)