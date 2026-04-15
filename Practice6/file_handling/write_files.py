from pathlib import Path

file_path = Path("example.txt")

#1 Write text (overwrite mode)
with open(file_path, "w", encoding="utf-8") as f:
    f.write("This is a new file\n")

#2 Write multiple lines using list
lines = ["Python\n", "File Handling\n", "Practice\n"]
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

#3 Append new data to file
with open(file_path, "a", encoding="utf-8") as f:
    f.write("Appended line\n")

#4 Write numbers using loop
with open(file_path, "w", encoding="utf-8") as f:
    for i in range(1, 6):
        f.write(f"Number {i}\n")

#5 Create and write to another file
new_file = Path("data.txt")
with open(new_file, "w", encoding="utf-8") as f:
    f.write("New file created\n")

#6 Append multiple lines
with open(new_file, "a", encoding="utf-8") as f:
    f.writelines(["Extra line 1\n", "Extra line 2\n"])