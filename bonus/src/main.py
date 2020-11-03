#!/usr/bin/env python3

from src import utils as u
from src import groundhog as g
import sys

def check_args():
    if len(sys.argv) != 2:
        u.print_and_quit(u.my_errno.get(0));
    if sys.argv[1] == "-h":
        u.print_help()
    try:
        val = int(sys.argv[1])
    except:
        u.print_and_quit(u.my_errno.get(1))
    try:
        if val <= 0:
            raise ValueError
    except ValueError:
        u.print_and_quit(u.my_errno.get(3));

def main():
    check_args()
    g.groundhog(int(sys.argv[1]))

if __name__ == "__main__":
    main()