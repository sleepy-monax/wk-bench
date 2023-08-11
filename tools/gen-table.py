#!/usr/bin/env python3

"""
Generate big html table with random data

Usage:
    gendata.py <rows> <cols>  > <output>
"""

import random
import string

def main():
    import sys
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    print("<table>")
    for i in range(rows):
        print("<tr>")
        for j in range(cols):
            print("<td>%d %d %s</td>" % (i, j, random.choice(string.ascii_letters)))
        print("</tr>")
    print("</table>")
 

if __name__ == '__main__':
    main()
