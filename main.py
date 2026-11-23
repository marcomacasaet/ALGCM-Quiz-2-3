import organizing_cleaned_data
import Identifier
import csv

def writeFile(variants_log):
    
    with open('Variants.csv','w',newline='') as variantsCsv:
        fields = ["word1","word2","word1_count","word2_count","character_difference"]
        write = csv.DictWriter(variantsCsv,fieldnames=fields)
        write.writeheader()
        write.writerows(variants_log)
    
def main():
    allwords_dtb = organizing_cleaned_data.organize_cleaned_data()
    variants_log = Identifier.identify(allwords_dtb, len(allwords_dtb))

    #print(len(allwords_dtb))
    #print(len(variants_log))

    for i in range(len(variants_log)):
        for key in variants_log[i]:
            print(key, " Count: ", variants_log[i][key], "\n")


if __name__ == "__main__":
    main()
