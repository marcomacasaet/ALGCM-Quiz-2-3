import csv
import organizing_cleaned_data
import Identifier


def writeFile(variants_log):

    with open("Variants.csv", "w", newline="") as variantsCsv:

        fields = [
            "word1",
            "word2",
            "word1_count",
            "word2_count",
            "character_difference"
        ]

        writer = csv.DictWriter(
            variantsCsv,
            fieldnames=fields
        )

        writer.writeheader()
        writer.writerows(variants_log)


def main():

    print("Loading dataset...")

    allwords_dtb = organizing_cleaned_data.organize_cleaned_data()
    print("Unique words found:", len(allwords_dtb))
    
    variants_log = Identifier.new_identify(allwords_dtb,len(allwords_dtb))
    print("Variants found:", len(variants_log))

    writeFile(variants_log)
    print("Variants written to Variants.csv")

    # Optional debugging output
    """
    for variant in variants_log:

        for key in variant:
            print(
                key,
                ":",
                variant[key]
            )

        print()
    """


if __name__ == "__main__":
    main()
