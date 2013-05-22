import pickle
f = open('banner.p', 'r')
banner = pickle.load(f)
for line in banner:
	print ''.join(map(lambda x: x[0]*x[1], line))
