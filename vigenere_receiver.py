#!/usr/bin/python



# default values
PIPE = "buffer"
KEY = "hola"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
EXTRA_NUMBERS = "0123456789"
EXTRA_CAPITAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


if __name__ == "__main__":

    f = open(PIPE,"r",0)
    
    print "Zi\tXi"

    for i in range(0,10):
        Zi_character = f.read(1) 
        Zi = ALPHABET.find( Zi_character )
        key_pos = i % 4
        Yi = ALPHABET.find( KEY[key_pos] )
        Xi = (Zi - Yi) % 26
        Xi_character = ALPHABET[Xi]
        print Zi_character + "\t" + Xi_character



    f.close()            
