def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = len(file_contents.split(" "))
    
    
    print(num_words," words found in the document")

main()