import random

import typer
from rich import get_console

# init a console for fancy printing
console = get_console()

# init the app for fast command app programming
app = typer.Typer()


@app.command()
def shuffle_letters(fname: str):
    # open txt file with the text
    with open(fname, "r") as f:
        lines = f.readlines()

    # remove attached marker for a new line '\n'
    lines = [line.rstrip("\n") for line in lines]

    # init a list of lines to place the new lines with shuffled words
    mixed_lines = []
    # iterate over every line
    for line in lines:
        # init a list of words for each line
        mixed_line = []
        # split the line by white space ' ' and iterate over every word in the line
        for word in line.split(" "):
            # list(...) will create an array of every character in the word
            # but only use the 2nd until the char before the last, indexing starting with 0,
            # hence, 1 to -1 (<- second last index)
            sub_word = list(word)[1:-1]
            # with `shuffle` the list gets shuffled, inplace, thus no need to get the output
            random.shuffle(sub_word)

            # join the first, shuffled and last character of a word
            new_word = word[0] + "".join(sub_word) + word[-1]

            # append new word to `mixed_line`
            mixed_line.append(new_word)
        mixed_lines.append(" ".join(mixed_line))

    # let the console print the shuffled words
    console.print("\n".join(mixed_lines))


if __name__ == "__main__":
    app()
