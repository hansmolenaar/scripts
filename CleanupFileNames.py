#!/usr/bin/env python3
import sys
import re
import MyStringLib

from MyStringLib import removeLeadinngBlanks
from MyStringLib import removeTrailingBlanks
from MyStringLib import removeMultipleBlanks
from MyStringLib import replaceOddCharacters
from MyStringLib import stripLeadingDoubleQuote
from MyStringLib import stripTrailingDoubleQuote

# Generate file list with ls -1 -Q > list.txt

def transform(name):
    retval = name

    retval, hasLeadingDoubleQuote = stripLeadingDoubleQuote(retval)
    retval, hasTrailingDoubleQuote = stripTrailingDoubleQuote(retval)
    retval = replaceOddCharacters(retval)
    retval = removeLeadinngBlanks(retval)
    retval = removeTrailingBlanks(retval)
    retval =removeMultipleBlanks(retval)

    if hasLeadingDoubleQuote:
       retval = "\"" + retval
    if hasTrailingDoubleQuote:
      retval = retval + "\""
    return retval

def main():
    with open('list.txt') as f:
        for oldName in f.read().splitlines():
            newName = transform(oldName)
            if (oldName != newName):
               sys.stdout.write(oldName + " -> " + newName + "\n"  )

if __name__ == '__main__':
    main()
