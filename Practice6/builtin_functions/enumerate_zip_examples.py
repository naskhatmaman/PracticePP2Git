names = ["Ali", "Dana", "Aruzhan"]
scores = [85, 90, 78]

#1 Use enumerate
for i, name in enumerate(names):
    print(f"{i}: {name}")

#2 Enumerate starting from 1
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

#3 Use zip for pairing
for name, score in zip(names, scores):
    print(f"{name} -> {score}")

#4 Convert zip to dictionary
students = dict(zip(names, scores))
print("Dictionary:", students)

#5 Type conversion
value = "100"
print("Converted:", int(value))

#6 Use len on list
print("Total students:", len(names))