#most inefficent code ever answer is 232792560

number=1
notDone=True

def generateList(number):
	list=[]
	works=True
	for x in range(1,21):
		
		if(number!=x):
			list.append(number%x)
	for t in list:
		if(t!=0):
			works=False
			return works
	return works

while(notDone):
	works=generateList(number)
	if(works):
		print "Number found " + str(number)
		notDone=False

	number=number+1
	print str(number)