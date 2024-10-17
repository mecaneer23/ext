#!/usr/bin/env python3

"""
Return the file extensions for passed in files
"""

from sys import argv


def main(args: list[str]) -> None:
    """Print file extensions for passed in files"""
    for arg in args:
        if "." not in arg:
            print(f"`{arg}` doesn't have a file extension")
            continue
        print(arg.rpartition(".")[-1])


if __name__ == "__main__":
    main(argv[1:])
