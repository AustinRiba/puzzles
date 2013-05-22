def main(message):
	readable = ""
	for char in message:
		ascii = ord(char)
		if(ascii == 32 or ascii == 46 or ascii == 40 or ascii == 41 or ascii == 39):
			result = ascii
		else:
			if(ascii+2 < 122):
				result = ascii+2
			else:
				result = ascii+2-26
		readable += unichr(result)
	print("%s") % readable
jarbled = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print("First Message: ")
main(jarbled)
url = "map"
print("url: ")
main(url)
