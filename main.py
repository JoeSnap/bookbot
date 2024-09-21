def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(file_contents)


def num_of_words(input):
    words = input.split()
    return len(words)

def num_of_letters(input):
    lowered_input = input.lower()
    letters = {}
    for letter in lowered_input:
        if letter in letters:
            letters[letter] += 1
            continue
        letters[letter] = 1
    return letters

def print_report(input):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words(input)} words found in the document")
    print("")
    letters = num_of_letters(input)
    for letter in letters:
        if (not letter.isalpha()) :
            continue
        print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End report ---")

main()