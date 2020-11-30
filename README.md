# Small Misc Tools

Here are some misc tools I wrote.

## NumberToAscii_BaseDecode

This script can do some digital to ASCII code conversion, and can carry out cyclic base decoding.

#### example

Run the command for help
```
python3 NumberToAscii_BaseDecode --help
```

the output
```
usage: NumberToAscii_BaseDecode.py [-h] [-H] [-B] [-a] [-b] [-f]

Some code conversion tools, including ASCII code to hexadecimal code, hexadecimal to ASCII code, binary to ASCII code, base decoding and so on

optional arguments:
  -h, --help      show this help message and exit
  -H , --hex      Enter a hexadecimal number to convert to an ASCII code
  -B , --binary   Enter a binary number to convert to an ASCII code
  -a , --ascii    Enter an ASCII code to convert to hexadecimal code
  -b , --base     Base nested decryption
  -f , --file     Base text file to decrypt
```

The H parameter is used to convert a string of hexadecimals to a string
example:
```
python3 NumberToAscii_BaseDecode.py -H 0x616263646566
```
the output:
```
########################################
[*] HEX to the ASCII code is :  b'abcdef'
########################################
```

The B parameter is used to convert a string of binary to a string
example:
```
python3 NumberToAscii_BaseDecode.py -B 01001000  
```
the output:
```
########################################
[*] BINARY to the ASCII code is :  b'H'
########################################
```

The a parameter is used to convert a string to a string of hexadecimals
example:
```
python3 NumberToAscii_BaseDecode.py -a "Hello World" 
```
output:
```
########################################
[*] ASCII code to the HEX is :  b'48656c6c6f20576f726c64'
########################################
```

Parameter b is used to decrypt a section of base code. At present, it supports the cyclic decryption of base16, base32, Base64 and base85.
example:
```
python3 NumberToAscii_BaseDecode.py -b VTBkV2MySkhPR2RXTWpsNVlrZFJQUT09    (three times base64 encode)
```
output:
```
########################################
[*] Base Decode is :  Hello World
########################################
```

Parameter f to support file decryption in the form of loop.
```
python3 NumberToAscii_BaseDecode.py -f /Users/lemon/Desktop/misc/enclosure/compi/LC/Final/misc1/bassssse.txt
```
output:
```
########################################
[*] Base Decode is :  flag{4b057431c3ee0c4f56d4dad18c352375}
########################################
```

