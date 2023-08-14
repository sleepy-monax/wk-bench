#!/usr/bin/env python3

"""
Generate big html table with random data

Usage:
    gendata.py <rows> <cols>  > <output>
"""

import random
import string

WORDS = [
    'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing',
    'elit', 'curabitur', 'vel', 'hendrerit', 'libero', 'eleifend', 'blandit',
    'nunc', 'ornare', 'odio', 'ut', 'orci', 'gravida', 'imperdiet', 'nullam',
    'purus', 'lacinia', 'a', 'pretium', 'quis', 'congue', 'praesent', 'sagittis',
    'laoreet', 'auctor', 'mauris', 'non', 'velit', 'eros', 'dictum', 'proin',
    'accumsan', 'sapien', 'nec', 'massa', 'volutpat', 'venenatis', 'sed',
    'eu', 'molestie', 'lacus', 'quisque', 'porttitor', 'ligula', 'dui',
    'mollis', 'tempus', 'at', 'magna', 'vestibulum', 'turpis', 'ac', 'diam',
    'tincidunt', 'id', 'condimentum', 'enim', 'sodales', 'in', 'hac',
    'habitasse', 'platea', 'dictumst', 'aenean', 'neque', 'fusce', 'augue',
]

def random_string(length):
    return ' '.join(random.sample(WORDS, length))


def main():
    import sys
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    print("<body>")
    print("<table>")
    for i in range(rows):
        print("<tr>")
        for j in range(cols):
            print("<td>%s</td>" % random_string(j + 1))
        print("</tr>")
    print("</table>")
    print("</body>")
 

if __name__ == '__main__':
    main()
