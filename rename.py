#!/usr/bin/env python3
import sys
import re
import MyStringLib

# Generate file list with ls -1 -Q > list.txt

from MyStringLib import removeLeadinngBlanks
from MyStringLib import removeTrailingBlanks
from MyStringLib import removeMultipleBlanks
#from MyStringLib import replaceOddCharacters
from MyStringLib import stripLeadingDoubleQuote
from MyStringLib import stripTrailingDoubleQuote

def removeTrackNumber(name):
    retval = re.sub("\\d+\\." , "", name)
    return retval

def stripExtension(name):
    return re.sub(".mp3" , "", name)

def markNoHyphen(name):
    if (name.count('-') == 0):
        return "@" + name
    return name

def checkDoubleQuotes(name):
    if (name.count('\"') != 0):
        sys.exit(name)
    return name

def markDoubleQuotes(name):
    return re.sub("\"" , "@", name)

def swapTitleArtist(name):
    checkSingleHyphen(name)
    parts = name.split('-')
    return parts[1] + " - " + parts[0]

def cleanYear(name):
    retval =  name
    retval = re.sub("\\{1965}" , " (1965)", retval)
    retval = re.sub("\\{1966}" , " (1966)", retval)
    retval = re.sub("\\{1967}" , " (1967)", retval)
    retval = re.sub("\\{1968}" , " (1968)", retval)
    retval = re.sub("\\{1969}" , " (1969)", retval)
    retval = re.sub("\\( 19" , " (19", retval)
    return retval

def replaceOddCharacters(name):
    retval =  name
    retval = re.sub("-" , "-", retval)
    retval = re.sub("\\.＊" , "", retval)
    retval = re.sub("＊" , "", retval)
    retval = re.sub("＂" , "", retval)
    retval = re.sub("：" , "", retval)
    retval = re.sub("：" , "", retval)
    retval = re.sub("‎" , " ", retval)
    return retval

def replaceDotDotMp3(name):
    return re.sub("\\.\\.mp3" , ".mp3", name)

def markMetaInfo(name):
    retval =  name
    retval = re.sub("garage" , "[garage", retval)
    retval = re.sub("Garage" , "[Garage", retval)
    retval = re.sub("GARAGE" , "[GARAGE", retval)
    return retval

def transform(name):
    retval = name
    #retval = checkSingleHyphen(retval)
    retval, hasLeadingDoubleQuote = stripLeadingDoubleQuote(retval)
    retval, hasTrailingDoubleQuote = stripTrailingDoubleQuote(retval)
    #retval = checkDoubleQuotes(retval)
    retval = markNoHyphen(retval)
    #retval = markDoubleQuotes(retval)
    retval = replaceDotDotMp3(retval)
    retval = stripExtension(retval)
    #retval = removeTrackNumber(retval)
    #retval = swapTitleArtist(retval)
    retval = removeLeadinngBlanks(retval)
    retval = removeTrailingBlanks(retval)
    retval = cleanYear(retval)
    retval = replaceOddCharacters(retval)
    retval = removeMultipleBlanks(retval)
    #retval = markMetaInfo(retval)

    retval = retval + ".mp3"
    if hasLeadingDoubleQuote:
       retval = "\"" + retval
    if hasTrailingDoubleQuote:
      retval = retval + "\""
    return retval;
    
def main():
    with open('list.txt') as f:
        for oldName in f.read().splitlines():
            newName = transform(oldName)
            if (oldName != newName):
                sys.stdout.write("mv " +  oldName + "  " + newName + "\n"  )


if __name__ == '__main__':
    main()
