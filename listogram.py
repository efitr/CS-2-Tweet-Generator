
source_text = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

#stringify(source)

def listogram(source_text):
    full_list = []
    for word in source_text:

        if word not in full_list:
            full_list.append([word,source_text.count(word)])

    listogram = []
    for word in full_list:
        if word not in listogram:
            listogram.append(word)

    return listogram

listo= listogram(source_text)

print (listo)
