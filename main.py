from itertools import count


def read_file():
    with open("sample.txt", "r") as file:
        sample = file.read()
    return sample

def count_lines():
    lines = read_file().split("\n")
    return len(lines)

def count_words():
    words = read_file().split()
    return len(words)

def count_word(word):
    words = read_file().split()

    count = 0

    for item in words:
        if item == word:
            count += 1
    return count

def find_longest_word():
    words = read_file().split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def find_word(word):
    words = read_file().split()

    for item in words:
        if item == word:
            return item
    return None

def count_characters():
    characters = read_file()
    return len(characters)