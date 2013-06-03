import Image
im = Image.open('oxygen.png')
pix = im.load()
width = im.size[0]
height = im.size[1]
pixels = [115]
last = pix[0,45][0]
for j in range(width):
	if pix[j,45][0] != last:
		pixels.append(pix[j,45][0])
		last = pix[j,45][0]
result = ""
for letter in pixels:
	if letter < 127:
		result+= str(unichr(letter))
sentance = result[:-18]
print sentance
