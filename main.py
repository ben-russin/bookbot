def count_letters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def count_words(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count



def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        letter_counts = count_letters(file_contents)
        word_counts = count_words(file_contents)

        # Sort the letter_counts dictionary by value in descending order
        sorted_letter_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

        # Print the formatted report
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_counts} words found in the document\n")
        for letter, count in sorted_letter_counts:
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")

if __name__ == "__main__":
    main()
