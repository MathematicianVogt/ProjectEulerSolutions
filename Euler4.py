
#finds the largest paladrone number on interval a-b
def isPadaladrone(number):
	numberString=str(number)
	if(str(numberString) == str(numberString)[::-1]):
		return True
	else:
		return False

a=100
b=1000
largestPal=0
listOfPaladroneNumbers=[]
for x in range(a,b):
	for y in range(a,b):
		currentMulti=x*y
		if(isPadaladrone(currentMulti) and currentMulti>largestPal):
			largestPal=currentMulti
			print str(currentMulti)
			listOfPaladroneNumbers.append(currentMulti)

print "Largest number found at " + str(listOfPaladroneNumbers[-1])
