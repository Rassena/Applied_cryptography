import os
from pathlib import Path


ASCII_MOD=128

def read_file(file: Path) -> str:
    with open(file, encoding="ASCII") as f:
        lines = f.readlines()
        return ''.join(lines)


def write_file(file: Path, text: str):
    with open(file, "w", encoding="ASCII") as f:
        f.write(text)


def one_time_pad(text: str, password: str) -> str:
    pass


def main():
    """Main program"""
    text = read_file("./plain.txt")
    write_file("./substitute_proprietary.txt", text)
    print(text.encode())
    return 0


if __name__ == "__main__":
    main()
