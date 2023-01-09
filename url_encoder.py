#!/usr/bin/env python3
from argparse import ArgumentParser
from sys import stdin, stdout, argv
from urllib.parse import quote as url_encode


def all_url_encode(string, repeat=1):
    for _ in range(repeat):
        string = "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)
    return string

def normal_url_encode(string, repeat=1):
    for _ in range(repeat):
        string = url_encode(" ".join(string))
    return string

def main():
    parser = ArgumentParser()
    parser.add_argument("-a", "--all", help="Encode every character", action="store_true")
    parser.add_argument("-d", "--double", help="Double URL encode to bypass some LFI restriction", action="store_true" )
    parser.add_argument("string", nargs="*")
    args = parser.parse_args()

    if args.double:
        repeat = 2
    else:
        repeat = 1

    if args.string:
        if args.all:
            print(all_url_encode(" ".join(args.string), repeat))
        else:
            print(normal_url_encode(" ".join(args.string), repeat))
    else:    
        print("Please provide a string to encode")

if __name__ == '__main__':
    main()