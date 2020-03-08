lexicon ={}
for directions in['north','south','east','west']:
    lexicon.update({directions:'direction})
for verbs in ['go','stop']:
    lexicon.update({verbs:'verb'})
for stop in ['the','in']
    lexicon.update({stops:'stop'})
for nouns in ['door','bear']
    lexicon.update({nouns,'noun'})
for numbers in [2,3,4]
    lexicon.update({numbers,'number'})

stuff=raw_input('>')
words=stuff.lower.split()
def scan(sentence):
    words=sentence.split()
    result=[]
    for word in words:
    try:
        k=words.lower()
        result.append(lexicon[k],word)
    except KeyError:
        if convert_number(word)!=None: 
            result.append('number',int(word))
        else:
            result.append('error',word))

    return result

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None




      
    

    
