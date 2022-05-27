# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import re
def read_file_content(filename):
    # [assignment] Add your code here 
    res = ""
    with open(filename, 'r') as f:
        for line in f:
            res += line
    return res

def count_words(text = read_file_content("./story.txt")):
    
    # [assignment] Add your code here]]
    
    new_text = re.findall('[^!\n.? ]+', text.lower()) #remove unwanted characters 
    word_count = {}
    for word in new_text:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    return word_count

print(count_words())