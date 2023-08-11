from xml.etree import ElementTree

def copy_attributes(src, dst, exclude=None):
    """
    Copies all attributes from src to dst. If exclude is not None, the
    attributes in exclude are not copied.

    :param src: The source element
    :param dst: The destination element
    :param exclude: A list of attributes that should not be copied
    """
    if exclude is None:
        exclude = []
    for key, value in src.attrib.items():
        if key not in exclude:
            dst.set(key, value)

def split_table(etree, max_rows):
    """
    Walks through the etree and splits tables with more than max_rows rows into
    multiple tables with max_rows rows.

    This function is needed because wkhtmltopdf has a exponential memory growth
    when processing tables with many rows. This function is a workaround for
    this problem.

    :param etree: The etree to process
    :param max_rows: The maximum number of rows per table
    """
    index = 0
    for child in etree:
        if child.tag == 'table' and len(child) > max_rows:
            etree.remove(child)

            first = True
            rows = list(child)
            while len(rows) > 0:
                table = ElementTree.Element('table')
                etree.insert(index, table)
                
                # We don't want to copy the id attribute because it is
                # unique and we want to avoid duplicate ids
                copy_attributes(child, table, exclude=None if first else ['id'])
                table.extend(rows[:max_rows])

                index += 1
                first = False
                rows = rows[max_rows:]
        else:
            split_table(child, max_rows)
            index += 1


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: {} <max_rows> <input>".format(sys.argv[0]))
        sys.exit(1)
    max_rows = int(sys.argv[1])
    etree = ElementTree.parse(sys.argv[2])
    split_table(etree.getroot(), max_rows)
    print(ElementTree.tostring(etree.getroot(), encoding='unicode'))

