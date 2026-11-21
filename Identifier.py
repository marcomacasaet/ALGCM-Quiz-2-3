"""
This module assumes the data is given in a 2D array in the format [word][wordcount], wherein the dataset is clean of unnecessary special characters.
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
    cdiffs = { ("d", "r"), ("e", "i"), ("o", "u"), ("uw", "w"), ("iy", "y"), ("eh", "ih"), ("om", "um"), ("uw", "w"), ("c", "k"), ("o", "w"), ("i", "y"), ("b", "v") }

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
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                original = "" + word1[i]
                difference = "" + word1[i] + word2[i]

                if followsRules(original, difference):
                    return original, difference, True

    # For letter replacements
    elif len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                original = "" + word1[i]
                difference = "" + word1[2]

                # CorV checks consistency of sandwiching letters to filter out words from other languages
                if "" + CorV(word1[i-1]) + CorV(word1[i+1]) == "" + CorV(word2[i-1]) + CorV(word2[i+1]) and followsRules(original, difference):
                    return original, difference, True

    else: 
        return original, difference, False

"""
allwords    : list      - list of all words in the dataset, including typos, plus their wordcount (sorted by word count)
uq          : int       - Total amt. of unique word spellings

returns variants_log (a list of dictionaries with all the relevant spelling variants)
"""
def identify(allwords, uq):
    existing = [] # list of existing words
    variants_log = [] # list of logs (dictionaries) of spelling variants
    avg = 0

    for i in range(uq):
        avg += allwords[i]["Count"]
    avg = avg / uq

    for i in range(uq):
        if allwords[i]["Fil_word"] not in existing:
            for j in range(len(existing)):
                levenshtein = levenshteinDistance(allwords[i]["Fil_word"], existing[j]["Fil_word"])       
                # for levenshtein distance 1 , with same first and last letter
                if levenshtein == 1 and allwords[i]["Fil_word"][0] == existing[j]["Fil_word"][0] and allwords[i]["Fil_word"][len(allwords[i]["Fil_word"])] == existing[j]["Fil_word"][len(existing[j]["Fil_word"])]:
                    orig, diff, isVar = isVariant(allwords[i]["Fil_word"], existing[j]["Fil_word"])   
                    if isVar:
                        variants_log.append({"word1": existing[j]["Fil_word"], "word2": allwords[i]["Fil_word"], "word1_count": existing[j]["Count"], "word2_count": allwords[i]["Count"], "character_difference": diff + " vs. " + orig})
                        break
            else:
                existing.append(allwords[i]["Fil_word"])
            
    return variants_log


