#!/usr/bin/python


import sys
import argparse
import random

# default values
PIPE = "buffer"
KEY = "hola"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
EXTRA_NUMBERS = "0123456789"
EXTRA_CAPITAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ALPHABET_SIZE = 26
KEY_SIZE = 4
END_STREAMING = '?'

def add_more_characters(extra):
    """ this function will add more characters to the default alphabetic

    args:
        extra: these extra characters include numbers, capital letter,
               or other defined characters by the user"""
    global ALPHABET

    if extra == "capital":
        ALPHABET += EXTRA_CAPITAL
    elif extra == "numbers":
        ALPHABET += EXTRA_NUMBERS
    else:
        ALPHABET += extra


if __name__ == "__main__":
    global ALPHABET_SIZE
    global KEY_SIZE

    parser = argparse.ArgumentParser(description="Encrypt plain text using Vigenere algorithm")
    parser.add_argument('-k', '--key', help='key used to encrypt the plain text')
    parser.add_argument('-p','--pipe', help='name of pipe')
    parser.add_argument('-e','--expand-alphabet',help='add a defined list of characters to the alphabet.\
                  "numbers" - add numbers from 0 to 9, "capital" - add capital letters, or a list of strings')
    parser.add_argument('--eos', help="character to end streaming")

    args = parser.parse_args()
    # check if we need to increase the number of characters in the alphabet
    if args.expand_alphabet != None:
        add_more_characters(args.expand_alphabet)
    ALPHABET_SIZE = len( ALPHABET )

    # if a new key is given, then do not generate a new one
    if args.key != None:
        KEY = args.key

    KEY_SIZE = len(KEY)

    # enter the character used to finish communication
    if args.eos != None:
        END_STREAMING = args.eos


    # print some useful information to share with the receiver
    print "ALPHABET: " + ALPHABET
    print "number of characters: " + str( ALPHABET_SIZE )
    print "KEY: " + KEY
    print "size of key: " + str( KEY_SIZE )
    print ""
    print "pipe name : " + PIPE
    print "character to stop streaming: " + END_STREAMING
    print ""

    print "Zi\tXi"

    # open the pipe and disable buffering
    with open(PIPE,"r",0) as f:

        i = 0

        while True:
            Zi_character = f.read(1) 
            if Zi_character == END_STREAMING:
                break

            Zi = ALPHABET.find( Zi_character )
            key_pos = i % KEY_SIZE
            Yi = ALPHABET.find( KEY[key_pos] )

            # apply Vigenere to decrypt
            Xi = (Zi - Yi) % ALPHABET_SIZE
            Xi_character = ALPHABET[Xi]

            print Zi_character + "\t" + Xi_character
            i += 1            
