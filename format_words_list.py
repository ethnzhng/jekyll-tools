import os

# Read the list of words from the input file
with open("words.txt", "r") as file:
    words = file.read().splitlines()

words = [word.lower() for word in words]

result = "[\n"
for i, word in enumerate(words):
    if i < len(words) - 1:
        result += f'  "{word}",\n'
    else:
        result += f'  "{word}"\n'
result += "]"

# Write the result to the output file
with open("output.txt", "w") as file:
    file.write(result)

print("The json array of words has been saved to output.txt")
