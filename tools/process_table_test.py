#!/usr/bin/env python3

from process_table import split_table
from xml.etree import ElementTree

SIMPLE_XML = """
<root>
    <table>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>2</td>
            <td>2</td>
            <td>2</td>
        </tr>
        <tr>
            <td>3</td>
            <td>3</td>
            <td>3</td>
        </tr>
    </table>
</root>
"""

def cleanup_string(s):
    return ''.join(s.strip().replace('\n', '').split())

def compare(actual, expected):
    return cleanup_string(actual) == cleanup_string(expected)

def test_case(description, actual, expected, max_rows):
    print(description, end='... ');
    etree = ElementTree.fromstring(actual)
    split_table(etree, max_rows)
    actual = ElementTree.tostring(etree, encoding='unicode')
    assert compare(actual, expected), "Failed\nExpected:\n{}\n\nActual:\n{}".format(expected, actual)
    print("Passed")
    
if __name__ == '__main__':
    test_case("Table's len is equal to max_rows", SIMPLE_XML, SIMPLE_XML, 3)
    test_case("Split every rows", SIMPLE_XML, """
    <root>
        <table>
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
        </table>
        <table>
            <tr>
                <td>2</td>
                <td>2</td>
                <td>2</td>
            </tr>
        </table>
        <table>
            <tr>
                <td>3</td>
                <td>3</td>
                <td>3</td>
            </tr>
        </table>
    </root>
    """, 1)
    
    test_case("Common case", SIMPLE_XML, """
    <root>
        <table>
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
            <tr>
                <td>2</td>
                <td>2</td>
                <td>2</td>
            </tr>
        </table>
        <table>
            <tr>
                <td>3</td>
                <td>3</td>
                <td>3</td>
            </tr>
        </table>
    </root>
    """, 2)
    
    test_case("Nested tables should be handled", """
    <root>
        <table>
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
            <tr>
                <td>2</td>
                <td>2</td>
                <td>2</td>
            </tr>
            <tr>
                <td>3</td>
                <td>3</td>
                <td>3</td>
            </tr>
            <tr>
                <td>
                    <table>
                        <tr>
                            <td>4</td>
                            <td>4</td>
                            <td>4</td>
                        </tr>
                        <tr>
                            <td>5</td>
                            <td>5</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>6</td>
                            <td>6</td>
                            <td>6</td>
                        </tr>
                    </table>
                </td>
                <td>7</td>
                <td>7</td>
            </tr>
        </table>
    </root>
    """, """
    <root>
        <table>
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
            <tr>
                <td>2</td>
                <td>2</td>
                <td>2</td>
            </tr>
        </table>
        <table>
            <tr>
                <td>3</td>
                <td>3</td>
                <td>3</td>
            </tr>
            <tr>
                <td>
                    <table>
                        <tr>
                            <td>4</td>
                            <td>4</td>
                            <td>4</td>
                        </tr>
                        <tr>
                            <td>5</td>
                            <td>5</td>
                            <td>5</td>
                        </tr>
                    </table>
                    <table>
                        <tr>
                            <td>6</td>
                            <td>6</td>
                            <td>6</td>
                        </tr>
                    </table>
                </td>
                <td>7</td>
                <td>7</td>
            </tr>
        </table>
    </root>
    """, 2)


    test_case("Nested tables should be handled", """
    <root>
        <table>
            <tr>
                <td>
                    <table>
                        <tr>
                            <td>4</td>
                            <td>4</td>
                            <td>4</td>
                        </tr>
                        <tr>
                            <td>5</td>
                            <td>5</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>6</td>
                            <td>6</td>
                            <td>6</td>
                        </tr>
                    </table>
                </td>
                <td>7</td>
                <td>7</td>
            </tr>
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
            <tr>
                <td>2</td>
                <td>2</td>
                <td>2</td>
            </tr>
            <tr>
                <td>3</td>
                <td>3</td>
                <td>3</td>
            </tr>
        </table>
    </root>
    """, """
    <root>
        <table>
            <tr>
                <td>
                    <table>
                        <tr>
                            <td>4</td>
                            <td>4</td>
                            <td>4</td>
                        </tr>
                        <tr>
                            <td>5</td>
                            <td>5</td>
                            <td>5</td>
                        </tr>
                    </table>
                    <table>
                        <tr>
                            <td>6</td>
                            <td>6</td>
                            <td>6</td>
                        </tr>
                    </table>
                </td>
                <td>7</td>
                <td>7</td>
            </tr>
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
        </table>
        <table>
            <tr>
                <td>2</td>
                <td>2</td>
                <td>2</td>
            </tr>
            <tr>
                <td>3</td>
                <td>3</td>
                <td>3</td>
            </tr>
        </table>
    </root>
    """, 2)
            
    test_case("Copy attributes attributes should be copied", """
    <root>
        <table class="fancy-style">
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
            <tr>
                <td>
                <td>2</td>
                <td>2</td>
                <td>2</td>
                </td>
            </tr>
        </table>
    </root>
    """, """
    <root>
        <table class="fancy-style">
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
        </table>
        <table class="fancy-style">
            <tr>
                <td>
                    <td>2</td>
                    <td>2</td>
                    <td>2</td>
                </td>
            </tr>
        </table>
    </root>
    """, 1)
    test_case("Except the id attribute which shouldn't be copied", """
    <root>
        <table id="1">
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
            <tr>
                <td>
                <td>2</td>
                <td>2</td>
                <td>2</td>
                </td>
            </tr>
        </table>
    </root>
    """, """
    <root>
        <table id="1">
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
            </tr>
        </table>
        <table>
            <tr>
                <td>
                    <td>2</td>
                    <td>2</td>
                    <td>2</td>
                </td>
            </tr>
        </table>
    </root>
    """, 1)  
    print()
    print("All tests passed")

