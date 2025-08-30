from array import*
a1 = array('i', [23,43,34])
a1.append(10)
for i in range(len(a1)):
	print(a1[i], end=' ')
    
a1.insert(1, 100)
for i in range(len(a1)):
    print(a1[i], end=' ')   