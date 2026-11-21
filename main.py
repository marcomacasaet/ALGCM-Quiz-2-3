def main():
    allwords_dtb = organize_cleaned_data()
    variants_log = identify(allwords_dtb, len(allwords_dtb))

    #print(len(allwords_dtb))
    #print(len(variants_log))

    for i in range(len(variants_log)):
        for key in variants_log[i]:
            print(key, " Count: ", variants_log[i][key], "\n")


if __name__ == "__main__":
    main()
