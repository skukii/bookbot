from stats import get_num_words, mapping_chars
import sys

def main():
    arguments = sys.argv

    if len(arguments) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = arguments[1]

    with open(book) as f:
        file_contents = f.read()
    
    num_words = get_num_words(file_contents)
    chars = mapping_chars(file_contents)


    print("============ BOOKBOT ============")
    print("Analyzing book found at ", book, "...")
    print("----------- Word Count ----------")
    
    print("Found ", num_words," total words")
    print("--------- Character Count -------")
    sorted_chars = sorted(
        chars.items(), 
        key=lambda item: item[1],
        reverse=True               
    )
    
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    
    print("============= END ===============")



main()