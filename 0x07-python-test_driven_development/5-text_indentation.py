#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ?, and :.

    Args:
    text (str): the text to be printed

    Raises:
    TypeError: if `text` is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split text into a list of words
    words = text.split()

    # Iterate through the list of words
    for i, word in enumerate(words):
        print(word, end="")
        if word[-1] in ".?:":
            print()
            print()
        elif i < len(words) - 1:
            print(" ", end="")
