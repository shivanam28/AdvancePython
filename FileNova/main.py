
from pathlib import Path



# FileNova - File & Folder Manager
BASE_DIR = Path(__file__).resolve().parent
WORKSPACE = BASE_DIR / "workspace"

# Create workspace if it doesn't exist
WORKSPACE.mkdir(exist_ok=True)


def get_path():
    """Get a path inside the workspace."""
    name = input("Enter file/folder name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return None

    path = (WORKSPACE / name).resolve()

    # Prevent operations outside the workspace
    if not path.is_relative_to(WORKSPACE.resolve()):
        print("Error: Access outside workspace is not allowed.")
        return None

    return path


def create_file():
    path = get_path()
    if path is None:
        return

    if path.exists():
        print("File or folder already exists.")
        return

    if path.parent != WORKSPACE.resolve():
        print("Please use an existing folder in the workspace.")
        return

    try:
        path.touch()
        print("File created successfully!")
    except OSError as error:
        print(f"Error creating file: {error}")


def read_file():
    path = get_path()
    if path is None:
        return

    if not path.is_file():
        print("File does not exist.")
        return

    try:
        print("\n--- File Content ---")
        print(path.read_text(encoding="utf-8"))
        print("--------------------")
    except (OSError, UnicodeError) as error:
        print(f"Error reading file: {error}")


def update_file():
    path = get_path()
    if path is None:
        return

    if not path.is_file():
        print("File does not exist.")
        return

    print("Enter the new content for the file:")
    content = input("> ")

    try:
        path.write_text(content, encoding="utf-8")
        print("File updated successfully!")
    except OSError as error:
        print(f"Error updating file: {error}")


def delete_file():
    path = get_path()
    if path is None:
        return

    if not path.is_file():
        print("File does not exist.")
        return

    confirm = input(f"Delete '{path.name}'? (y/n): ").strip().lower()

    if confirm == "y":
        try:
            path.unlink()
            print("File deleted successfully!")
        except OSError as error:
            print(f"Error deleting file: {error}")
    else:
        print("Deletion cancelled.")


def create_folder():
    path = get_path()
    if path is None:
        return

    if path.exists():
        print("File or folder already exists.")
        return

    if path.parent != WORKSPACE.resolve():
        print("Please create folders directly inside the workspace.")
        return

    try:
        path.mkdir()
        print("Folder created successfully!")
    except OSError as error:
        print(f"Error creating folder: {error}")


def rename_item():
    path = get_path()
    if path is None:
        return

    if not path.exists():
        print("File or folder does not exist.")
        return

    new_name = input("Enter the new name: ").strip()

    if not new_name or new_name in {".", ".."}:
        print("Invalid name.")
        return

    # Only allow renaming within the same directory
    if Path(new_name).name != new_name or "/" in new_name or "\\" in new_name:
        print("Enter a name only, without a path.")
        return

    new_path = path.with_name(new_name)

    if new_path.exists():
        print("A file or folder with that name already exists.")
        return

    try:
        path.rename(new_path)
        print("Renamed successfully!")
    except OSError as error:
        print(f"Error renaming: {error}")


def delete_folder():
    path = get_path()
    if path is None:
        return

    if not path.is_dir():
        print("Folder does not exist.")
        return

    if any(path.iterdir()):
        print("Folder is not empty. Delete its contents first.")
        return

    confirm = input(f"Delete folder '{path.name}'? (y/n): ").strip().lower()

    if confirm == "y":
        try:
            path.rmdir()
            print("Folder deleted successfully!")
        except OSError as error:
            print(f"Error deleting folder: {error}")
    else:
        print("Deletion cancelled.")


def view_directory():
    print(f"\nWorkspace: {WORKSPACE}")

    items = sorted(WORKSPACE.iterdir(), key=lambda item: item.name.lower())

    if not items:
        print("Workspace is empty.")
        return

    print("\n--- Files & Folders ---")
    for item in items:
        kind = "[DIR] " if item.is_dir() else "[FILE]"
        print(f"{kind} {item.name}")


def main():
    while True:
        print("\n" + "=" * 36)
        print("       FileNova Manager")
        print("=" * 36)
        print("1. Create File")
        print("2. Read File")
        print("3. Update File")
        print("4. Delete File")
        print("5. Create Folder")
        print("6. Rename File/Folder")
        print("7. Delete Folder")
        print("8. View Directory")
        print("9. Exit")
        print("=" * 36)

        choice = input("Enter your choice: ").strip()

        operations = {
            "1": create_file,
            "2": read_file,
            "3": update_file,
            "4": delete_file,
            "5": create_folder,
            "6": rename_item,
            "7": delete_folder,
            "8": view_directory,
        }

        if choice == "9":
            print("Thank you for using FileNova. Goodbye!")
            break

        operation = operations.get(choice)

        if operation:
            operation()
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
