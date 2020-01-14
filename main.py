'''
take any file type (power point, txt, word, etc and replace whatever words u want, as many times as you like.
if 3 times, then only first 3, add another input maybe last 3 words. if put -1 then means change all words

'''
lines = -1      #reads all lines of file
words = -1      #replaces all words in file

def wordReplacer(text, wordDict):
    for key in wordDict:
        text = text.replace(key, wordDict[key])
    return text


f = open("assignment2.txt", "r")
text = f.read()

wordDic = {
'original word' : 'new word',
'Armen': 'Andrei',
}

newText = wordReplacer(text, wordDic)

#create a new file with new text
file = open("newfile.txt","w+")
file.write(newText)