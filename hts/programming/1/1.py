def permutation(string):
	if string == "":
		return [string]
	else:
		ans = []
		for anagram in permutation(string[1:]):
			for pos in range(len(anagram)+1):
				ans.append(anagram[:pos]+string[0]+anagram[pos:])
		return ans

def dictionary(wordlist):
	dict = {}
	infile = open(wordlist, "r")
	for line in infile:
		word = line.split("\n")[0]
		word = word.lower()
		word = word.replace('\r','')
		dict[word] = 1
	infile.close()
	return dict

def main():
	diction = dictionary("wordlist.txt")
	print diction
	words = raw_input("enter a word: \n")
	wordlst = words.split(',')
	solutionLst = []
	for word in wordlst:
		anaLst = permutation(word)
		for ana in anaLst:
			if diction.has_key(ana):
				diction[ana] = word
				if ana not in solutionLst:
					solutionLst.append(ana)
				print "The solution to the jumble is is", ana
	s = ""
	for solution in solutionLst:
		s+=solution+","
	print s
	
main()
