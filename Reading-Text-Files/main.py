# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, "r") as file:
        data = file.read()
        data = data.split(' ')
    return data


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    flist = []
    clist = []
    count = 0
    bagOfWords = []
    for word in text:
        if (word != ''):
            if(word[:1] != '\n'):
                bagOfWords.append(word)
            elif(word[:1] == '\n'):
                word = word[1:]
                bagOfWords.append(word)
            # bagOfWords.append(word)
    for first in bagOfWords:
        for second in bagOfWords:
            if first == second:
                count += 1
        flist.append(first)
        clist.append(count)
        result = dict(zip(flist,clist))
        count = 0
    return result #{"as": 10, "would": 20}
result = count_words()
print(result)
