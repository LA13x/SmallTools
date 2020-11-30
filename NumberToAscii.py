import sys
import binascii
import argparse

'''
@ Some code conversion tools, including ASCII code to hexadecimal code
@ hexadecimal to ASCII code, binary to ASCII code, base decoding and so on 
'''

parser = argparse.ArgumentParser(description = "Some code conversion tools, including ASCII code to hexadecimal code, hexadecimal to ASCII code, binary to ASCII code, base decoding and so on ")
parser.add_argument("-H",'--hex',type = str,metavar = '',required = False,help = "Enter a hexadecimal number to convert to an ASCII code")
parser.add_argument("-B",'--binary',type = str,metavar = '',required = False,help = "Enter a binary number to convert to an ASCII code")
parser.add_argument("-a",'--ascii',type = str,metavar = '',required = False,help = "Enter an ASCII code to convert to hexadecimal code")

args = parser.parse_args()

def hex_to_ascii(Hex):
	if "0x" in Hex:
		Hex = Hex[2:]
	asc = binascii.unhexlify(Hex)
	return asc

def bin_to_ascii(Bin):
	if "0b" in Bin:
		Bin = Bin[2:]
	Bin = int(Bin,base = 2)
	Bin = hex(Bin)
	Bin = Bin[2:]
	asc = binascii.unhexlify(Bin)
	return asc

def ascii_to_hex(asc):
	Hex = binascii.hexlify(asc)
	return Hex

if __name__ == '__main__':
	Hex = args.hex
	Bin = args.binary
	if Hex == None and Bin == None:
		print("Please `python3 NumberToAscii.py -h (or --help)`")
		exit()
	
	if Hex != None : 
		Ascii = hex_to_ascii(Hex)
		print("[*]ascii:",Ascii)

	if Bin != None :
		Ascii = bin_to_ascii(Bin)
		print("[*]ascii:",Ascii)

	

