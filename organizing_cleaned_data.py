def organize_cleaned_data():
    #print("program starting")

    # Fil_word and Count are now stored as: { word, count }
    Sorted_DB = {}

    # Opening the TXT file
    with open("Processed.txt", mode='r') as f:

        #print("reading")

        for line in f:

            line = line.strip()

            #print("counting")

            #if the word is already in the database, increment the count
            if line in Sorted_DB:
                Sorted_DB[line] += 1
            #if the word is not in the database, add it to the database with a count of 1
            else:
                #print("adding")
                Sorted_DB[line] = 1

    # prints the word and the count of the word in the database, not yet sorted by count
    #for Fil_word in Sorted_DB:
    #    print(Fil_word, " Count: ", Sorted_DB[Fil_word], "\n")


    # sorts the database by count in descending order
    DB_by_count = sorted(Sorted_DB.items(),key=lambda count: count[1],reverse=True) #uncomment the following lines to print the sorted database by count (WIP)

    #for Fil_word, Count in DB_by_count:
        #print(Fil_word, " Count: ", Count, "\n")

    #converting touples to dictionaries, mb I thought they were interchangable
    DB_by_count_dict = []
    for Fil_word, Count in DB_by_count:
        DB_by_count_dict.append(
            {
                "Fil_word": Fil_word,
                "Count": Count
            }
        )
        
    #print("program finished running")
    return DB_by_count_dict
