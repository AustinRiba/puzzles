import zipfile
import re
channel = zipfile.ZipFile('channel.zip', 'r')
print(channel.open('readme.txt').read())
hint = ""

def getNext(num):
	global hint
	findnothing = re.compile(r"nothing is (\d+)").search
	zipItemText = channel.open(num+'.txt').read()
	match = findnothing(zipItemText)
	if match:
		zipItemInfo = channel.getinfo(num+'.txt')
		hint+=zipItemInfo.comment
		nothing = match.group(1)
		getNext(nothing)
	else:
		print zipItemText

getNext('90052')
print hint
print "it's in the air, look at the letters... oxygen!"
