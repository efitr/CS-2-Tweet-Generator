
source_text = "one fish two fish red fish blue fish"

stringify(source)

def histogram(self, source_text):
    histogram = {}
    for word in source_text:
        if word not in histogram:
            histogram[word] = 0
        histogram[word] += 1
    return histogram


