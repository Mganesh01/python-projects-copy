"""Examples for reading, writing, appending, and seeking in files."""

from pathlib import Path


def create_student_file(path: Path) -> None:
    """Create a sample students file if it does not already exist."""
    students = [
        "Alice - Python\n",
        "Bob - Java\n",
        "Charlie - Data Science\n",
        "Diana - Web Development\n",
        "Ethan - AI\n",
    ]
    path.write_text("".join(students), encoding="utf-8")


def demonstrate_file_modes(path: Path) -> None:
    """Read, update, append, and move the file pointer."""
    with path.open("r", encoding="utf-8") as file:
        print("Complete content:")
        print(file.read())

    with path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    lines[1] = "Bharat - Python\n"

    with path.open("w", encoding="utf-8") as file:
        file.writelines(lines)

    with path.open("a", encoding="utf-8") as file:
        file.write("Karthik - Java\n")

    with path.open("r", encoding="utf-8") as file:
        file.seek(10)
        print(f"Current file pointer position: {file.tell()}")


if __name__ == "__main__":
    student_file = Path("students.txt")
    create_student_file(student_file)
    demonstrate_file_modes(student_file)
