import organizing_cleaned_data
import Identifier
import csv



"""
This module contains functions to identify spelling variants in a list of words. 
It uses the Levenshtein distance algorithm to compare words and determine if they are variants of each other based on specific rules and conditions. 
The identified variants of certain words are logged in a list of dictionaries.
The main function of this module is "new_identify", which organizes words into buckets based on their first letter, last letter, and length, and compares only similar words to reduce processing time. The module also includes helper functions for calculating Levenshtein distance, checking if a character is a consonant or vowel, and determining if one word is a variant of another based on specific conditions.
For documentation purposes, "old_identify" and other dependant functions were kept despite not being utilized anymore
"""

#Levenshtein distance using Iterative with the full matrix approach by geeks4geeks
#The iterative technique with a full matrix uses a 2D matrix to hold the intermediate results of the Levenshtein distance calculation. It begins with empty strings and iteratively fills the matrix row by row. It computes the minimum cost of insertions, deletions, and replacements based on the characters of both strings. 
def levenshteinDistance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Initialize a matrix to store the edit distances
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize the first row and column with values from 0 to m and 0 to n respectively
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the matrix using dynamic programming to compute edit distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Characters don't match, choose minimum cost among insertion, deletion, or substitution
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    # Return the edit distance between the strings
    return dp[m][n]


"""
Returns C for consonants and V for vowels.
"""
def CorV (char):
    if char in ['a', 'e', 'i', 'o', 'u']:
        return "V"
    else:
        return "C"

"""
Check if the difference specified is valid based on a set of rules/trends.
Returns True if difference is valid and False otherwise.
"""
def followsRules(a, b):
    cdiffs = { ("d", "r"), ("e", "i"), ("o", "u"), ("uw", "w"), ("iy", "y"), ("eh", "ih"), ("om", "um"), ("uw", "w") }

    # a is always longer
    if len(a) < len(b):
        c = a
        a = b
        b = c

    if (a, b) in cdiffs or (b, a) in cdiffs:
        return True
    else:
        return False

"""
Check if one Filipino word is the variant of another using specific conditions.
Assumes the words have a levenshtein distance of 1.

Returns the difference letters as original, difference and True if one word is a variant of the other.
"""
def isVariant(word1, word2):
    original, difference = "", ""

    # word2 is always longer
    if len(word1) > len(word2):
        temp = word1
        word1 = word2
        word2 = temp

    # For letter insertions
    if len(word1) != len(word2):
        word1 += " "

        for i in range(len(word2)):
            if word1[i] != word2[i]:
                original = "" + word1[i]
                difference = "" + word1[i] + word2[i]

                if followsRules(original, difference):
                    return original, difference, True

    # For letter replacements
    elif len(word1) == len(word2):

        for i in range(len(word1)):

            if word1[i] != word2[i]:

                original = word1[i]
                difference = word2[i]

                # CorV checks consistency of sandwiching letters
                # to filter out words from other languages

                # First or last character has no sandwich
                if i == 0 or i == len(word1) - 1:
                    sandwich_match = True

                else:
                    sandwich_match = (
                        CorV(word1[i - 1]) +
                        CorV(word1[i + 1])
                        ==
                        CorV(word2[i - 1]) +
                        CorV(word2[i + 1])
                    )

                if sandwich_match and followsRules(original, difference):
                    return original, difference, True
                    

    return original, difference, False

"""
allwords    : list      - list of all words in the dataset, including typos, plus their wordcount (sorted by word count)
uq          : int       - Total amt. of unique word spellings

returns variants_log (a list of dictionaries with all the relevant spelling variants)
"""
def old_identify(allwords, uq):
    existing = [] # list of existing words
    variants_log = [] # list of logs (dictionaries) of spelling variants
    existing.append(allwords[0])
    explored = []
    wordcounter = uq
    found = False

    for i in range(1, uq):
        print("> Checking for variant ! :3")

        for j in range(len(existing)):
            
            sameSandwich = True if allwords[i]["Fil_word"].startswith(existing[j]["Fil_word"][0]) and allwords[i]["Fil_word"].endswith(existing[j]["Fil_word"][-1]) else False
            
            if len(allwords[i]["Fil_word"]) == len(existing[j]["Fil_word"]) and sameSandwich:
                # length comparison base for levenshtein
                levenshtein = abs(len(allwords[i]["Fil_word"]) - len(existing[j]["Fil_word"])) 
                

                # only use actual levenshtein to find words that need replacement, for shortening processing time
                if levenshtein == 0 or (levenshtein == 1 and sameSandwich):
                    levenshtein = levenshteinDistance(allwords[i]["Fil_word"], existing[j]["Fil_word"])     
                    
                # for levenshtein distance 1 , with same first and last letter
                if levenshtein == 1 and sameSandwich:
                    orig, diff, isVar = isVariant(allwords[i]["Fil_word"], existing[j]["Fil_word"])   
                    if isVar:
                        variants_log.append({"word1": existing[j]["Fil_word"], "word2": allwords[i]["Fil_word"], "word1_count": existing[j]["Count"], "word2_count": allwords[i]["Count"], "character_difference": diff + " vs. " + orig})
                        print("> Words until program ends: ", wordcounter, "> Variant added ! :> ", variants_log[-1]["word1"], " MATCH ", variants_log[-1]["word2"])
                        found = True
                        break
                else:
                    print("> Words until program ends: ", wordcounter, "> Not matched ! :c || word: ", allwords[i]["Fil_word"], "vs.", existing[j]["Fil_word"])
                    found = False
                
        if not found:
            print("> No variant found ! :c || word: ", allwords[i]["Fil_word"])
            existing.append(allwords[i])
            
        wordcounter-=1
    
    print("> Variant identification complete !! Variants log length : ", len(variants_log))
    return variants_log

"""
allwords    : list      - Alphabetically sorted list of dictionaries, containing all unique words and respective counts
uq          : int       - Total amount of unique word spellings
"""
def new_identify(allwords, uq):
    # this function identifies spelling variants in a list of words using a more efficient approach by organizing words into buckets based on their first letter, last letter, and length. It compares only similar words to reduce processing time.
    from rapidfuzz.distance import Levenshtein #speeds up levenshtein distance calculation
    
    # an empty list to store the identified variants
    variants_log = []

    # a dictionary to store existing buckets of words based on their first letter, last letter, and length
    existing_buckets = {}

    # Add the first word
    first_word = allwords[0]

    # Create a bucket key based on the first letter, last letter, and length of the first word
    first_key = (
        first_word["Fil_word"][0].lower(),
        first_word["Fil_word"][-1].lower(),
        len(first_word["Fil_word"])
    )

    existing_buckets[first_key] = [first_word]

    wordcounter = uq

    for i in range(1, uq):
        # for checking 
        #print("> Checking for variant ! :3")

        current_word = allwords[i]["Fil_word"]
        
        # get the first letter, last letter, and length of the current word
        first_letter = current_word[0].lower()
        last_letter = current_word[-1].lower()
        word_length = len(current_word)

        found = False

        # Search only similar buckets
        candidate_list = []

        #consider words that are one letter shorter, same length, or one letter longer
        for length_bucket in (
            word_length - 1,
            word_length,
            word_length + 1
        ):

            # create a bucket key based on the first letter, last letter, and length of word
            bucket_key = (
                first_letter,
                last_letter,
                length_bucket
            )

            # if the bucket exists, add its words to the candidate list
            if bucket_key in existing_buckets:
                candidate_list.extend(existing_buckets[bucket_key])

        # compare only against candidates to save processing time
        for candidate in candidate_list:

            candidate_word = candidate["Fil_word"]

            # skip if the current word is the same as the candidate word
            if current_word == candidate_word:
                continue


            # check the length difference between the current word and the candidate word
            length_diff = abs(len(current_word) - len(candidate_word))

            if length_diff > 1:
                continue
                
            # calculate the Levenshtein distance between the current word and the candidate word    
            distance = Levenshtein.distance(current_word,candidate_word,score_cutoff=1)

            if distance == 1:
                
                orig, diff, isVar = isVariant(current_word,candidate_word)
                
                if isVar:
                    # add the identified variant to the variants_log
                    variants_log.append(
                        {
                            "word1": candidate["Fil_word"],
                            "word2": current_word,
                            "word1_count": candidate["Count"],
                            "word2_count": allwords[i]["Count"],
                            "character_difference":
                                diff + " vs. " + orig
                        }
                    )
                    '''
                    #checking pace of program
                    if (wordcounter % 10000 == 0):
                        print(
                            "> Words until program ends:",
                            wordcounter,
                            "> Variant added! :>",
                            variants_log[-1]["word1"],
                            "MATCH",
                            variants_log[-1]["word2"]
                        )
                    '''

                    found = True
                    break

        if not found:
            '''
            print(
                "> No variant found! :c || word:",
                current_word
            )
            '''
            # create a new bucket for the current word based on its first letter, last letter, and length
            bucket_key = (
                first_letter,
                last_letter,
                word_length
            )

            # if the bucket is not found in existing_buckets, create it and add the current word to it
            if bucket_key not in existing_buckets:
                existing_buckets[bucket_key] = []

            # add the current word to the appropriate bucket in existing_buckets
            existing_buckets[bucket_key].append(allwords[i])

        wordcounter -= 1

    print("> Variant identification complete !! Variants log length:", len(variants_log))

    return variants_log

