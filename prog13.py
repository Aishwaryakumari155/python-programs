lines = [
    "This is the first line.",
    "And here's the second line.",
    "The third line concludes the example."
]

with open("another_file.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")  