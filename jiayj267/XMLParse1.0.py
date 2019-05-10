"""
  Author:  JYJ
  Purpose: Parse the xml file
  Created: 29/1/2018
"""
from lxml import etree
from io import StringIO

class XMLParse():

    def __init__(self):
        '''

        '''

    def xmlparse(self,filepath):
        path_to_file = filepath
        for event, element in etree.iterparse(path_to_file, events=('end',)):
            dic = {}
            for child in element.iter():
                if child.text == None:
                    dic[child.tag] = child.attrib
                else:
                    dic[child.tag] = child.text
            return dic
            element.clear()

def main():
    parsexml = XMLParse()
    parsexml.xmlparse('C:/Users/jiayj/Desktop/full database.xml')

if __name__=='__main__':
    main()
