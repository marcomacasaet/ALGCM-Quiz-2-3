# This function organizes the cleaned data from the Processed.txt file into a list of dictionaries, 
# where each dictionary contains a unique word and its count. 
# The words are sorted in ascending order.
def organize_cleaned_data():

    print("program starting")

    Sorted_DB = {}
    
    # Opening the TXT file
    with open("Processed.txt", mode='r') as f:
        
        #loop through each line in the file
        for line in f:

            line = line.strip()
            #if the word is already in the database, increment the count
            if line in Sorted_DB:
                Sorted_DB[line] += 1
            else:
                Sorted_DB[line] = 1

    #sort the database by word in ascending order
    DB_by_A_Z = sorted(
        Sorted_DB.items(),
        key=lambda word: word[0]
    )
    
    # convert the sorted tuples into a list of dictionaries
    DB_by_A_Z_dict = []

    for Fil_word, Count in DB_by_A_Z:

        DB_by_A_Z_dict.append(
            {
                "Fil_word": Fil_word,
                "Count": Count
            }
        )

    print("program finished running")

    return DB_by_A_Z_dict
