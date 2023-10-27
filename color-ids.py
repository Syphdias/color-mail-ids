#!/usr/bin/env python3
from sys import stdin
import re

COLORS = [
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[34m",
    "\033[35m",
    "\033[36m",
]

COLOR_RESET = "\033[0m"

current_color_index = 0
MAX_NUM_ID = len(COLORS)
known_ids = [0 for _ in range(MAX_NUM_ID)]

if __name__ == "__main__":
    # exim
    #p = re.compile(r"([a-zA-Z0-9]{6}-[a-zA-Z0-9]{6}-[a-zA-Z0-9]{2})")
    # exim + postfix
    p = re.compile(r"([a-zA-Z0-9]{6}-[a-zA-Z0-9]{6}-[a-zA-Z0-9]{2}|[0-9A-F]{6,}|[0-9a-zA-Z]{12,})")
    for line in stdin:
        ids = re.findall(p, line)
        for i in ids:
            try:
                color_index = known_ids.index(i)
            except ValueError:
                # id not found in list
                known_ids[current_color_index] = i
                color_index = current_color_index
                if current_color_index < MAX_NUM_ID - 1:
                    current_color_index += 1
                else:
                    current_color_index = 0
            # substitute color in line
            line = re.sub(i, COLORS[color_index] + i + COLOR_RESET, line)
        print(line, end="")
