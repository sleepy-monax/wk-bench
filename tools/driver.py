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

GENERATORS = [
    ("splitted",'python ./tools/wkhtmltopdf-split.py'),
    ("normal",'wkhtmltopdf')
]

def main():
    if not os.path.exists(INDIR):
        os.mkdir(INDIR)
    
    if not os.path.exists(OUTDIR):
        os.mkdir(OUTDIR)

    if not os.path.exists(DATADIR):
        os.mkdir(DATADIR)

    for generator in GENERATORS:
        input_files = os.listdir(INDIR)
        for input_file in input_files:
            print('Processing {} using {}'.format(input_file, generator[0]))
            input_path = INDIR + input_file
            output_path = OUTDIR + input_file + '.' + generator[0] + '.pdf'
            data_path = DATADIR + input_file + '.' + generator[0] + '.csv'
            os.system('python3 tools/monitor.py 0.1 {} {}'.format(data_path, ' '.join([generator[1]] + sys.argv[1:] + [input_path, output_path])))

if __name__ == '__main__':
    main()
