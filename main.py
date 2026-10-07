
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

def analyze_file():
    choice = ""

    while choice != "7":
        print("Please select an option:")
        print("1. Count lines")
        print("2. Count words")
        print("3. Count specific word")
        print("4. Find longest word")
        print("5. Find a word")
        print("6. Count characters")  
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("Number of lines:", count_lines())

        elif choice == "2":
            print("Number of words:", count_words())

        elif choice == "3":
            word = input("Enter the word to count: ")
            print(f"Count of '{word}':", count_word(word))

        elif choice == "4":
            print("Longest word:", find_longest_word())

        elif choice == "5":
            word = input("Enter the word to find: ").strip()

            if not word:
                print("Invalid input. Please enter a valid word.")
            else:
                result = find_word(word)

                if result:
                    print(f"'{word}' found in the file.")
                else:
                    print(f"'{word}' not found in the file.")
            
        elif choice == "6":
            print("Number of characters:", count_characters())

        elif choice == "7":
            print("Exiting the program.")
            return

        else:
            print("Invalid choice. Please try again.")

analyze_file()

