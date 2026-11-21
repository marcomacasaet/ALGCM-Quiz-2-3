import csv

#Fil_word, and Count are the columns of the database
Sorted_DB = [
    ["", 0]
]

# Opening the CSV file
with open("Processed.txt", mode='r') as f: 
    
        for line in f:

            #if the word is already in the database, increment the count and break the loop
            for i in range(len(Sorted_DB)):
                if line == Sorted_DB[i][0]:
                    Sorted_DB[i][1] += 1
                    break

            #if the word is not in the database, add it to the database with a count of 1
            if line != Sorted_DB[i][0]:
                Sorted_DB.append([line, 1])

#prints the word and the count of the word in the database, not yet sorted by count
for i in range(len(Sorted_DB)):
    print(Sorted_DB[i][0], " Count: ", Sorted_DB[i][1], "\n")

#sorts the database by count in descending order
DB_by_count = sorted(Sorted_DB, key=lambda count: count[1], reverse=True) #uncomment the following lines to print the sorted database by count (WIP)
for i in range(len(DB_by_count)):
    print(DB_by_count[i][0], " Count: ", DB_by_count[i][1], "\n")