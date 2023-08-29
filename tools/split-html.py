#!/usr/bin/env python3

"""
A wrapper around wkhtmltopdf that process the input file in a way that
wkhtmltopdf can work faster.
"""

import os
import sys
import time
import tempfile
from xml.etree import ElementTree
from process_table import split_table


def main():
    if len(sys.argv) < 3:
        print('Usage: {} <input> <output>'.format(sys.argv[0]))
        sys.exit(1)

    start = time.time()
    etree = ElementTree.parse(sys.argv[1])
    split_table(etree.getroot(), 500)
    print('Splitting tables took {} seconds'.format(time.time() - start))
    etree.write(sys.argv[2], encoding='utf-8')


if __name__ == '__main__':
    main()
