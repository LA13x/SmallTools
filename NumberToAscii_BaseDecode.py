import base64
import binascii
import argparse

'''
@ Some code conversion tools, including ASCII code to hexadecimal code
@ hexadecimal to ASCII code, binary to ASCII code, base decoding
'''

parser = argparse.ArgumentParser(description = "Some code conversion tools, including ASCII code to hexadecimal code, hexadecimal to ASCII code, binary to ASCII code, base decoding and so on ")

parser.add_argument("-H",'--hex',type = str,metavar = '',required = False,help = "Enter a hexadecimal number to convert to an ASCII code")
parser.add_argument("-B",'--binary',type = str,metavar = '',required = False,help = "Enter a binary number to convert to an ASCII code")
parser.add_argument("-a",'--ascii',type = str,metavar = '',required = False,help = "Enter an ASCII code to convert to hexadecimal code")
parser.add_argument("-b",'--base',type = str,metavar = '',required = False,help = "Base nested decryption")
parser.add_argument("-f",'--file',type = str,metavar = '',required = False,help = "Base text file to decrypt")

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
	asc = bytes(asc,"ascii")
	Hex = binascii.hexlify(asc)
	return Hex

def base_decode(txt = None,filename = None):
	if txt == None and filename != None :
		with open(filename,"r") as f:
			text = f.read()
		while True:
			try:
				text = base64.b16decode(text).decode()
			except:
				try:
					text = base64.b32decode(text).decode()
				except:
					try:
						text = base64.b64decode(text).decode()
					except:
						try:
							text = base64.b85decode(text).decode()
						except:
							break
		return text

	if txt != None and filename == None :
		while True:
			try:
				txt = base64.b16decode(txt).decode()
			except:
				try:
					txt = base64.b32decode(txt).decode()
				except:
					try:
						txt = base64.b64decode(txt).decode()
					except:
						try:
							txt = base64.b85decode(txt).decode()
						except:
							break
		return txt


if __name__ == '__main__':
	Hex = args.hex
	Bin = args.binary
	Asc = args.ascii
	base = args.base
	file = args.file

	if Hex == None and Bin == None and Asc == None and base == None and file == None:
		print("Please `python3 NumberToAscii.py -h (or --help)` to get help :) ")
		exit()

	if Hex != None :
		Ascii = hex_to_ascii(Hex)
		print("########################################")
		print("[*] HEX to the ASCII code is : ",Ascii)
		print("########################################")

	if Bin != None :
		Ascii = bin_to_ascii(Bin)
		print("########################################")
		print("[*] BINARY to the ASCII code is : ",Ascii)
		print("########################################")

	if Asc != None :
		hexnumber = ascii_to_hex(Asc)
		print("########################################")
		print("[*] ASCII code to the HEX is : ",hexnumber)
		print("########################################")

	if base != None and file == None :	
		descryption = base_decode(base,None)
		print("########################################")
		print("[*] Base Decode is : ",descryption)
		print("########################################")

	if base == None and file != None :
		descryption = base_decode(None,file) 
		print("########################################")
		print("[*] Base Decode is : ",descryption)
		print("########################################")

	if base != None and file != None :
		print("When selecting a text file, you don't have to enter the string to decrypt!")


