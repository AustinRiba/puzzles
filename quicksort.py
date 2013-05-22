data = [1,6,7,2,3,3,10,15,23,2,4,19,22,24,99,0]
def quicksort(array):
	if len(array) <= 1:
		return array
	pivot = array.pop(len(array)/2)
	less = []
	greater= []
	for x in array:
		if x <= pivot:
			less.append(x)
		else:
			greater.append(x)
	final = []
	final.extend(quicksort(less))
	final.append(pivot)
	final.extend(quicksort(greater))
	return final
	
print quicksort(data)
