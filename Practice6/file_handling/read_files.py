from pathlib import Path

file_path = Path("example.txt")

#1 Read entire file content
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print("Full content:\n", content)

#2 Read file line by line with strip
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        print("Line:", line.strip())

#3 Read specific number of characters
with open(file_path, "r", encoding="utf-8") as f:
    partial = f.read(15)
    print("First 15 chars:", partial)

#4 Read first line only
with open(file_path, "r", encoding="utf-8") as f:
    first_line = f.readline()
    print("First line:", first_line)

#5 Read all lines into list and iterate
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        print(f"{i}: {line.strip()}")

#6 Check if file exists before reading
if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as f:
        print("File exists, length:", len(f.read()))