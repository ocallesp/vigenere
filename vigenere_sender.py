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

def key_generator(size):
    """ this function will generate a key of a given size

    args:
        size: size of the key"""
    

    
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



if __name__ ==  "__main__":
    global ALPHABET_SIZE
    global KEY_SIZE

    parser = argparse.ArgumentParser(description="Encrypt plain text using Vigenere algorithm")
    parser.add_argument('-k', '--key', help='key used to encrypt the plain text')
    parser.add_argument('-ks','--key-size', help='size of the key to generate')
    parser.add_argument('-p','--pipe', help='name of pipe')
    parser.add_argument('-e','--expand-alphabet',help='add a defined list of characters to the alphabet.\
                  "number" - add numbers from 0 to 9, "capital" - add capital letters, or a list of strings')
    parser.add_argument('--eos', help="character to end streaming")

    args = parser.parse_args()

    if args.expand_alphabet != None:
        add_more_characters(args.expand_alphabet)
    ALPHABET_SIZE = len( ALPHABET )

    if args.key != None:
        KEY = args.key
    else:
        if args.key_size != None:
            key_generator(key_size)

    if args.eof != None:
        END_STREAMING = args.eof


    KEY_SIZE = len(KEY)

    print "ALPHABET: " + ALPHABET
    print "number of characters: " + str( ALPHABET_SIZE )
    print "KEY: " + KEY
    print "size of key: " + str( KEY_SIZE )

    with open(PIPE,"w",0) as f:
        
        for i in range(0,10):
            Xi_character = raw_input()
            Xi = ALPHABET.find( Xi_character )
            key_pos = i % 4
            Yi = ALPHABET.find( KEY[key_pos] )
            Zi = (Xi + Yi) % 26
            Zi_character = ALPHABET[Zi]
            f.write( Zi_character )


    
