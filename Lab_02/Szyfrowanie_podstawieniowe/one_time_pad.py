import os
from pathlib import Path

def read_file(file: Path) -> str:
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
        return "\n".join(lines)


def write_file(file: Path, text: str):
    with open(file, "w", encoding="utf-8") as f:
        f.write(text)


def one_time_pad(text: str, password: str) -> str:
    pass


def main():
    """Main program"""
    text = read_file("./plain.txt")
    write_file("./substitute_proprietary.txt", text)
    return 0


if __name__ == "__main__":
    main()
