from stats import get_num_words, mapping_chars

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    
    num_words = get_num_words(file_contents)
    chars = mapping_chars(file_contents)


    print("============ BOOKBOT ============")
    print("Analyzing book found at ", path_to_file, "...")
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