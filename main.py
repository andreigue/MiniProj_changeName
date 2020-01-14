'''
take any file type (power point, txt, word, etc and replace whatever words u want.

'''

def wordReplacer(original_text, wordDict):
    for key in wordDict:
        new_Text = original_text.replace(key, wordDict[key])
    return new_Text


wordDic = {
'original word' : 'new word',
'karl': 'carl',
}

f = open("file1.txt", "r")
text = f.read()

newText = wordReplacer(text, wordDic)

#create a new file with new text
file = open("newfile.txt","w+")
file.write(newText)