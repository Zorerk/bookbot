

def count_words(words):
    count = 0
    len_count = words.split()
    count = len(len_count)
    print_word_report(count)

def count_letters(book):
    letter_count = {}
    for l in book:
        l = l.lower()
        if l in letter_count.keys():
            letter_count[l] += 1
        else: 
            letter_count.update({l: 1})
    print_letter_report(letter_count)

def print_word_report(word_count):
    print(f"{word_count} words found in the document")

def print_letter_report(letters):
    for letter in sorted(letters, key=letters.get, reverse=True):
        if letter.isalpha():
            print(f"The '{letter}' character was found {letters[letter]} times")
        else:
            pass

def main():
    with open("books/frankenstein.txt") as f:      
        file_contents = f.read()
        count_words(file_contents)
        count_letters(file_contents)
main()