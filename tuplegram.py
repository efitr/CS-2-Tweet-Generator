source_text = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']


def tuplegram(source_text):
    full_list = []
    for word in source_text:
        if word not in full_list:
            full_list.append((word,source_text.count(word)))

    tuples=[]
    for word in full_list:
        if word not in tuples:
            tuples.append(word)
    return tuples

tuple=tuplegram(source_text)
print(tuple)
