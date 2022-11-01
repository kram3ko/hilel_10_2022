from pathlib import Path
from typing import Generator

from pympler import asizeof

CURRENT_DIR = Path(__file__).parent
ROCKYOU_FILENAME = CURRENT_DIR / "rockyou.txt"
NEW_FILE = CURRENT_DIR / input("Please enter new filename: ")


def filter_lines(filename: Path, pattern: str) -> Generator:
    with open(filename, encoding="utf-8") as file:
        while True:
            line = file.readline()

            if not line:
                break

            if pattern in line.lower():
                yield line.replace("\n", "")


def main() -> None:
    """Function creating new file in currently directory,
    and write data what you choose in file"""
    count = 1
    with open(NEW_FILE, "w", encoding="utf-8") as file:
        for inp in filter_lines(ROCKYOU_FILENAME, input("what you want see:")):
            file.writelines(f"{str(count)} --> {inp} \n")
            count += 1


def count_lines() -> None:
    with open(NEW_FILE, "r", encoding="utf-8") as file:
        print(f"count lines new generated file = {len(file.readlines())}")
    len_file = len(open(ROCKYOU_FILENAME, "r", encoding="utf-8").readlines())
    print(f"count lines general file = {len_file}")


def size_of_file(file: Path):
    file_to_check = open(file, "r", encoding="utf-8").readlines()
    print(f"takes memory = {asizeof.asized(file_to_check, detail=1)}")


def options():
    """Function for option to check file size"""
    vars = {"original": ROCKYOU_FILENAME, "new": NEW_FILE, "exit": "exit"}
    print(f"What file you want check size or exit = {[i for i in vars]}")
    while True:
        selection = input("Enter file name: ")
        if selection == "original":
            size_of_file(vars["original"])
        elif selection == "new":
            size_of_file(vars["new"])
        elif selection == "exit":
            print("exiting ......  👋👋👋")
            break
        else:
            print(f"What file you want check size = {vars}")


if __name__ == "__main__":
    main()
    count_lines()
    options()
