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

    retval = re.sub("⧸" , "/", retval)
    retval = re.sub("？" , "?", retval)
    retval = re.sub("｜" , "|", retval)
    retval = re.sub("•" , "*", retval)
    retval = re.sub("´" , "'", retval)
    retval = re.sub("’" , "'", retval)
    retval = re.sub("º" , "o", retval)
    retval = re.sub("°" , "o", retval)
    retval = re.sub("ß" , "ss", retval)
    retval = re.sub("İ" , "I", retval)
    retval = re.sub("Ο" , "O", retval)

    retval = re.sub(str(chr(804)) , "", retval)
    retval = re.sub(str(chr(769)) , "", retval) # accent grave
    retval = re.sub(str(chr(776)) , "", retval) # trema
    retval = re.sub(str(chr(351)) , "s", retval) # Turks: s cedille
    retval = re.sub(str(chr(305)) , "i", retval) # Turks

    ignore = [193, 195, 209, 214, 216, 227, 220, 225, 228, 231, 232, 233, 237, 241, 243, 246, 252]
    for c in retval:
       ordc = ord(c)
       if (ordc > 127) and not (ordc in ignore):
         print(str(c) + " = " + str(ord(c)) +  " in " + retval)

    return retval

def stripLeadingDoubleQuote(name):
    retval = re.sub("^\"" , "", name)
    return retval, name != retval

def stripTrailingDoubleQuote(name):
    retval = re.sub("\"$" , "", name)
    return retval, name != retval
