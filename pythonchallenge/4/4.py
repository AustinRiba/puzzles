import urllib
def getNext(num, last):
	last = num
	s = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % num).read()
	s1 = s.find("is")+3
	num = s[s1:s1+5]
	if s == "Yes. Divide by two and keep going.":
		divideby = int(last)/2
		num = "%d" % divideby
	if not num.isdigit():
		print(s)
	getNext(num, last)
getNext("12345", "12345")
