#!/usr/bin/env python3
import sys
import re


# Generate file list with ls -1 -Q > list.txt

def removeLeadinngBlanks(name):
    return re.sub("^ +" , "", name)

def removeTrailingBlanks(name):
    return re.sub(" +$" , "", name)

def replaceMultipleBlanks(name):
    return re.sub("  +" , " ", name)

def removeTrackNumber(name):
    retval = re.sub("\\d+\\." , "", name)
    return retval

def stripLeadingDoubleQuote(name):
    return re.sub("^\"" , "", name)

def stripTrailingDoubleQuote(name):
    return re.sub("\"$" , "", name)

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
    retval = stripLeadingDoubleQuote(retval)
    retval = stripTrailingDoubleQuote(retval)
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
    retval = replaceMultipleBlanks(retval)
    #retval = markMetaInfo(retval)
    return "\"" + retval + ".mp3\""
    
def main():
    with open('list.txt') as f:
        for oldName in f.read().splitlines():
            newName = transform(oldName)
            if (oldName != newName):
                sys.stdout.write("mv " +  oldName + "  " + newName + "\n"  )


if __name__ == '__main__':
    main()
