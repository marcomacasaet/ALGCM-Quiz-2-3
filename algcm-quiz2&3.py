"""
Introduction by Marco

Okay, I will try to walk y'all through the idea here. The way I plan to do it is to 
divide the program into three main parts. These parts are as follows:

1. Reading and assigning - this is where the file will be read and assigned to the dictionary
2. Algorithm - this is when the algorithm will take place
3. Writing - this is when the final csv file is created that has the pairs

Please take note that for some of the comments, I might label them as "1.1" or "1.2" and so on and so forth
to denote functions that belong to a specific part of this program.
"""

def main():
    
    #Variable Declaration
    pair_list = list()
    
    word_database = readFile() #word database from the data set which will be read through the readFile() function
    
    pair_list.extend(sortThroughWords(word_database)) #this is where i plan to put the list of word-pair dictionaries
    
    writeFile(pair_list)
    
    return


#Part 1: Reading and Assigning

def readFile():
    
    word_database = None #i set is a no type muna
    
    #place and alter file read template here
    
    return word_database


#Part 2: Algorithm

def sortThroughWords(word_database):
    
    #this algorithm is where we will sort through the words
    #currently thinking of how to implement checkers to see if a word has been checked, current idea is a list
    
    pair_list = list()
    outerLoopWords = list()
    innerLoopWords = list()
    
    for word1 in word_database:
        #outer loop: mainly to run through words in the database
        #word1 is the focus here for the nested loop
        if word1 not in outerLoopWords: #we don't want to waste time repeating words
            for word2 in word_database: #okay highkey, this is medjo time inefficient pero like um... hindi naman kailangan na mabilis diba?
            #inner loop: word1 will compare with other words in the databases and get the edit distance as well as frequency
                if word2 not in innerLoopWords:
                    editDistance = levenshtein(word1, word2) #edit distance, to be honest i am thinking of returning levenshtein as a tuple. explanation later
                    wordFrequency = word_database.count(word1)/len(word_database) #how many times the word shows up in the data set
                #okay something we need to decide with the if statement is the threshold for the edit distance and word frequecny to determine if it is a variant
                    if variant is True: #placeholder, must be changed
                        word_pair = {
                            'word1' : word1, 
                            'word2' : word2,
                            'word1_count' : word_database.count(word1),
                            'word2_count' : word_database.count(word2),
                            'word1_character_difference' : None,
                            'word2_character_difference' : None
                        }
                        pair_list.append(word_pair)
                    innerLoopWords.append(word2)
        outerLoopWords.append(word1)
    
    return pair_list
                

def levenshtein(word1, word2):
    #i am thinking of a tuple here to store the edit distance and the different characters for both words
    
    return


#Part 3: Writing

def writeFile(pair_list):