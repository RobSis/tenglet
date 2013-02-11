#!/usr/bin/env python
# Licensed under the terms of the GPL v3. See LICENCE for details

import sys
import UserString
import getopt

VERSION = "Tenglet v0.9"
WIDTH = 80
fontfile = "tengwar.tlf"


class TengFont:
    def __init__(self, fontpath):
        self.data = open(fontpath).read().split('\n')
        if (self.data[0].strip()[:3] == "tlf"):
            tlf, self.height, self.max_length = self.data[0].strip().split(' ')
            self.unsup = 1

        else:
            print "Unsupported format or header."
            self.unsup = 0
            return None

        self.height = int(self.height)
        self.max_length = int(self.max_length)
        self.data = self.data[1:]
        self.message = list()
        for i in range(self.height):
            s = UserString.MutableString("")
            self.message += [s]

        self.tengchar = list()  # [ (char, left, right, data) ]
        x = -1
        for line in self.data:  # comments
            if (x > 0):
                if (line.find('@') <= self.max_length) and\
                   (line.find('@') != -1):
                    offset = line.find('@')
                else:
                    offset = self.max_length
                tempchar[3] += [line[:offset]]
                if (tempchar[0][:3] == "alt"):
                    tempchar[0] = chr(int(tempchar[0].split('/')[1]))
                x -= 1
            elif (x == 0):
                self.tengchar.append(tempchar)
                x = -1
            if (x == -1):
                tempchar = line.split()[:2] + [0] + [[]]
                try:
                    tempchar[1] = int(tempchar[1])
                except:
                    return None
                x = self.height

        return None

    def space(self, size):
        x = ""
        for i in range(size):
            x += " "
        return x

    def append(self, nchar):
        for i in range(self.height):
            offset = nchar[1] - len(nchar[3][i])

            if ((len(self.message[i]) - nchar[1]) < 0):
                self.message[i] = self.space(nchar[1] -\
                                    len(self.message[i])) + self.message[i]
                offset = 0

            if ((len(self.message[i]) - nchar[1] + len(nchar[3][i])) >\
                 len(self.message[i])):
                self.message[i] += self.space(len(nchar[3][i]) - nchar[1])
                offset = 0

            for x in range(len(nchar[3][i])):
                if (nchar[3][i][x] != ' '):
                    idx = len(self.message[i]) - len(nchar[3][i]) + x - offset
                    self.message[i][idx] = nchar[3][i][x]

        return 0

    def getletter(self, letter):
        for i in self.tengchar:
            if (chr(ord(i[0])) == chr(ord(letter))):
                return i

        return None

    def type(self, message):
        if not self.unsup:
            return ["Unsupported format or header"]
        for i in range(self.height):
            self.message[i] = UserString.MutableString("")
        for i in message:
            newlet = self.getletter(i)
            if (newlet == None):
                return ["Character not found: %d" % ord(i)]
            self.append(newlet)

        return self.message


def fileexist(filename):
    """fileexist(filename)->int|details

    Return zero when file was found or structure details when wasn't"""
    try:
        desc = open(filename, "r")
    except IOError, details:
        return details
    desc.close()
    return 0


def printhelp():
    print "Ussage:", sys.argv[0].split('/')[-1:][0], "[-f font] [-hv]"
    print
    print " --font=font     - Set font file (default tengwar.tlf)"
    print " --help          - This text"
    print " --version       - Print version and exit"


def printversion():
    print VERSION

# Getting options
ok = 1
try:
    opts, args = getopt.getopt(sys.argv[1:], "f:hv",
                            ["font=", "help", "version"])
except getopt.error:
    ok = 0

for opt, arg in opts:
    if (opt in ('-f', '--font')):
        if (fileexist(arg) == 0):
            fontfile = arg
        else:
            print >>sys.stderr, "Font file not found"
            sys.exit(1)
    if (opt in ('-h', '--help')):
        printhelp()
        sys.exit(0)
    if (opt in ('-v', '--version')):
        printversion()
        sys.exit(0)

banner = TengFont(fontfile)
while True:
        i = sys.stdin.readline()
        if (len(i) == 0):
                break
        i = i.strip("\t\n")
        if (i == ""):
                continue
        bar = banner.type(i)
        for x in bar:
                print x
