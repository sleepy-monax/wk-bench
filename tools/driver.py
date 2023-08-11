#!/usr/bin/env python3

"""
wkhtmltopdf benchmarking tool, it will generate a bunch of PDF files from the
input files in the input/ directory and record the time it takes to generate
each PDF file in the data.ignore/ directory.
"""

import os
import sys

INDIR = 'input/'
OUTDIR = 'output.ignore/'
DATADIR = 'data.ignore/'

def main():
    os.mkdir(INDIR)
    os.mkdir(OUTDIR)
    os.mkdir(DATADIR)

    input_files = os.listdir(INDIR)
    for input_file in input_files:
        input_path = INDIR + input_file
        output_path = OUTDIR + input_file + '.pdf'
        data_path = DATADIR + input_file + '.csv'
        os.system('python3 tools/monitor.py 0.1 {} {}'.format(data_path, ' '.join(['wkhtmltopdf'] + sys.argv[1:] + [input_path, output_path])))

if __name__ == '__main__':
    main()
