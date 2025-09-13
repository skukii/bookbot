from stats import get_num_words, mapping_chars

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    
    num_words = get_num_words(file_contents)
    chars = mapping_chars(file_contents)
    
    print(num_words," words found in the document")
    print(chars)



main()