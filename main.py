def count_words(words):
    count = 0
    len_count = words.split()
    count = len(len_count)
    print(count)


def main():
    with open("books/frankenstein.txt") as f:
        
        file_contents = f.read()
        count_words(file_contents)

main()