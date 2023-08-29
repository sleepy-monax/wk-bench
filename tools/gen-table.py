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
    print("<html>")
    print("""<head>
        <base href="http://localhost:8069" />
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link type="text/css" rel="stylesheet" href="/web/assets/debug/1/account_reports.assets_pdf_export.css" />
    </head>""")
    print("<body>")
    print("<table>")
    for i in range(rows):
        print("""
<tr tabindex="0" class="acc_rep_searchable acc_rep_level3  " style="">
                            <td class="acc_rep_name_ellipsis acc_rep_line acc_rep_line_indent  " colspan="1">
                                <span class="acc_rep_line_name">
                                    BILL/2023/08/0001
                                    <span class="acc_rep_footnote">
                                    </span>
                                </span>
                            </td>

                            <td>
                                <div class="acc_rep_column_value">
                                    <span class="acc_rep_column_value">08/14/2023</span>
                                </div>
                            </td>
                            <td>
                                <div class="acc_rep_column_value">
                                    <span class="acc_rep_column_value">[FURN_9999] Office Design Software</span>
                                </div>
                            </td>
                            <td>
                                <div class="acc_rep_column_value">
                                    <span class="acc_rep_column_value">Azure Interior</span>
                                </div>
                            </td>
                            <td>
                                <div class="acc_rep_column_value">
                                    <span class="acc_rep_column_value"
                                        style="display:block;text-align:right;">$ 20.00</span>
                                </div>
                            </td>
                            <td>
                                <div class="acc_rep_column_value">
                                    <span class="acc_rep_column_value"
                                        style="display:block;text-align:right;">$ 0.00</span>
                                </div>
                            </td>
                            <td>
                                <div class="acc_rep_column_value">
                                    <span class="acc_rep_column_value"
                                        style="display:block;text-align:right;">$ 30.00</span>
                                </div>
                            </td>

                        </tr>
""")
    print("</table>")
    print("</body>")
    print("</html>")


if __name__ == '__main__':
    main()
