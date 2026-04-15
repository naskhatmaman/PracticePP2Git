import shutil
from pathlib import Path

file_path = Path("example.txt")

#1 Copy file to new file
copy_path = Path("copy.txt")
shutil.copy(file_path, copy_path)

#2 Copy file to directory
backup_dir = Path("backup")
backup_dir.mkdir(exist_ok=True)
shutil.copy(file_path, backup_dir / "example_backup.txt")

#3 Copy with metadata
shutil.copy2(file_path, "copy_with_metadata.txt")

#4 Rename file
renamed = Path("renamed.txt")
if copy_path.exists():
    copy_path.rename(renamed)

#5 Delete file safely
if renamed.exists():
    renamed.unlink()

#6 Delete backup file
backup_file = backup_dir / "example_backup.txt"
if backup_file.exists():
    backup_file.unlink()