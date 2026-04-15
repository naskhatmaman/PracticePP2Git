import os

#1 Create a directory
if not os.path.exists("test_dir"):
    os.mkdir("test_dir")

#2 Create nested directories
os.makedirs("parent/child/grandchild", exist_ok=True)

#3 List all files and folders
items = os.listdir(".")
print("All items:", items)

#4 Filter only directories
dirs = [d for d in items if os.path.isdir(d)]
print("Directories:", dirs)

#5 Get current working directory
print("Current directory:", os.getcwd())

#6 Change directory and go back
os.chdir("parent")
print("Changed to:", os.getcwd())
os.chdir("..")