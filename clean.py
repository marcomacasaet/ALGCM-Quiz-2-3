

def readFile():
    
    allWords = list()
    sentence = list()
    
    with open("Raw.txt", "r", encoding="utf-8", errors="ignore") as f: 
        #this video helped a lot: https://www.youtube.com/watch?v=PNa9kVqZLIk
        
        for line in f:
            for word in line.split():
                try:
                    if '.' not in word and '?' not in word:
                        if word[-1].isalpha() == False:
                            word = word[:-1]
                        
                        if word[0].isalpha() == False:
                            word = word[1:]
                            
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
                if word:
                    if "'" in word or "-" in word:
                        f1.write(word)
                        f1.write("\n")
                        processedWords.append(word)
                    elif word.isalpha() == True:
                        f1.write(word)
                        f1.write("\n")
                        processedWords.append(word)
    
#print(processedWords) print statement for testing
    
