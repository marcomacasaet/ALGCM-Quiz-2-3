

def readFile():
    
    allWords = list()
    sentence = list()
    
    with open("Raw.txt", "r", encoding="utf-8", errors="ignore") as f: 
        #this video helped a lot: https://www.youtube.com/watch?v=PNa9kVqZLIk
        
        for line in f:
            for word in line.split():
                try:
                    if '.' not in word and '?' not in word:
                        sentence.append(word)
                    elif '.' in word:
                        fixedWord = word.replace(".","").strip()
                        sentence.append(fixedWord)
                        allWords.append(sentence.copy())
                        sentence.clear()
                    elif '?' in word:
                        fixedWord = word.replace("?","").strip()
                        sentence.append(fixedWord)
                        allWords.append(sentence.copy())
                        sentence.clear()
                except:
                    print("Exception. Not processing. Moving on.\n")
 
            
    return allWords

def hasNumber(word: str):
    
    for letter in word:
        if letter.isdigit():
            return True
    
    return False


def processWord(word : str):
    
    for letter in word:
        if letter.isalpha() == False:
            word.replace(letter,"").split()
    
    return word

allWords = readFile()
f1 = open("Processed.txt","w", encoding="utf-8", errors="ignore")
processedWords = list()
    
for sentence in allWords:
        
    startOfSentence = True
        
    for word in sentence:
        if word.isupper() == False and hasNumber(word) == False:
            if startOfSentence == True:
                word = word.lower()
                startOfSentence = False
            
            if word.isascii() == True and word.istitle() == False:
                if '-' in word or "'" in word or word.isalpha():
                    f1.write(word)
                    f1.write("\n")
                    processedWords.append(word)
                else:
                    word = processWord(word)
        
                if word:
                    f1.write(word)
                    f1.write("\n")
                    processedWords.append(word)
#print(processedWords) print statement for testing
    
