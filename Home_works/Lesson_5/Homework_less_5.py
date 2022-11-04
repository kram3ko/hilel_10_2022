from contextlib import contextmanager

colors = {
    "header": "\033[95m",
    "blue": "\033[94m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "endc": "\033[0m",
    "bold": "\033[1m",
    "underline": "\033[4m",
}


@contextmanager
def print_in_color(color):
    if colors.get(color) is None:
        yield print(f"{colors['endc']}no such a color --> default black")

    else:
        yield print(colors[color], end="")
        print(colors["endc"], end="")


def main():
    with print_in_color("red"):
        print("Hey it's write by red color")
    with print_in_color("ff"):
        print("wrong color")
    with print_in_color("blue"):
        print("Hey it's a blue color")

    print("endc color")


if __name__ == "__main__":
    main()
