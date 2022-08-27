
import time

print('Enter Text Please:')

data = input()


# conversion Chart
conversion_code = {
	
	# Uppercase Alphabets
	'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U',
    'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O',
    'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I',
    'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C',
    'Y': 'B', 'Z': 'A',

	# Lowercase Alphabets
	'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
	'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
	'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
	's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
	'y': 'b', 'z': 'a',

	'.': '+', '/': '!', '!': '/', '+': '.', ';': '#', '#': ';',
	':': '"', '"': ':', "'": '3', '3': "'", ' ': '<', '<': ' ',
	'’': '_', '_': '’', ',': '@', '@': ',', '=': '$', '$': '='
}

# Creating converted output
converted_data = ""


for i in range(0, len(data)):
	if data[i] in conversion_code.keys():
		converted_data += conversion_code[data[i]]
	else:
		converted_data += data[i]

# Creating the File for Encoded or Decoded file

my_file = open("Encoded-Decoded-data.txt","w+")
my_file.write("Encoded = " + converted_data + "\nDecoded = " + data)

print('Finished! Look for Encoded-Decoded-data.txt in your files!')
time.sleep(2)
