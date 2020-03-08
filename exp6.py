def break_words(stuff):
    words=stuff.split(' ')
    return words

def sorted_words(words):
    return sorted(words)

def print_first_word(words):
    word=words.pop(0)
    print word
def print_last_word(words):
    word=words.pop(-1)
    print word
def sort_sentence(sentence):
    words=break_words(sentence)
    return sorted_words(words)
def  first_last(sentence):
     word=break_words(sentence)
     print word.pop(0)
     print word.pop(-1)
def sorted_first_last(sentence):
     words=sorted_words(sentence)
     print word.pop(0)
     print word.pop(-1)
