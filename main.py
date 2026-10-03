def read_file():
    with open("sample.txt", "r") as file:
        sample = file.read()
    return sample

def count_lines():
    lines = read_file().split("\n")
    return len(lines)

print(count_lines())