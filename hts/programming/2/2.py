import Image
im = Image.open("PNG.png")
encoding = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '/': '-..-.',
        '8': '---..',           '(': '-.--.-',
        '9': '----.',           ')': '-.--.-',
        ' ': ' ',               '_': '..--.-',
}

decoding = {}
for key, val in encoding.items(): decoding[val] = key
def decode(message):
	ans = ''.join(map(lambda x, g=decoding.get: g(x, ' '), message.split(' ')))
	return ' '.join(ans.split())
	
def decipher(message):
    # like decode, but when there are no spaces.
    row = [ ( '', message ) ]
    while filter(lambda x: x[1], row):
        old = row
        row = []
        for it in old:
            txt, code = it
            if code:
                for (t, c) in encoding.items():
                    if code[:len(c)] == c:
                        row.append((txt + t, code[len(c):]))
                # NB we discard it if no initial segment of code matches an encoding.
            else: row.append(it)

    return map(lambda it: it[0], row)

def encode(text):
    # should really pre-process {'.': 'stop', ',': 'comma', '-': 'dash', ...}
    return ' '.join(map(lambda x, g=encoding.get: g(x, ' '), text.upper()))

pix = im.load()
width = im.size[0]
height = im.size[1]
arr = []
ascii = []
c = 0
last = 0
for i in range(height):
	row = []
	for j in range(width):
		if pix[j,i] == 1:
			ascii.append(c-last)
			last = c
		c+=1
		row.append(pix[j,i])
	arr.append(row)
print ascii

result = ""
for letter in ascii:
	result+= str(unichr(letter))
print result
print decode(result)
print encode("a test");
