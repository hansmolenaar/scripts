#!/usr/bin/env python3
import sys
import re

def removeLeadinngBlanks(name):
    return re.sub("^ +" , "", name)

def removeTrailingBlanks(name):
    return re.sub(" +$" , "", name)

def removeMultipleBlanks(name):
    return re.sub("  +" , " ", name)

def replaceOddCharacters(name):
    retval =  name
    retval = re.sub("-" , "-", retval)
    retval = re.sub("\\.＊" , "", retval)
    retval = re.sub("＊" , "", retval)
    retval = re.sub("＂" , "\"", retval)
    retval = re.sub("：" , ":", retval)
    retval = re.sub("：" , ":", retval)
    retval = re.sub("–" , "-", retval)
    retval = re.sub("~" , "-", retval)
    retval = re.sub("‎" , " ", retval)
    return retval

def stripLeadingDoubleQuote(name):
    retval = re.sub("^\"" , "", name)
    return retval, name != retval

def stripTrailingDoubleQuote(name):
    retval = re.sub("\"$" , "", name)
    return retval, name != retval
