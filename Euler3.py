#Most inefficent way to find the primes of a number: By fundamental thorem of arthematic.Given a big number, breaks down into prime numbers
number=2
primeList=[]
notDone=True
bigNumber=47

def dividesSomething(number):
		divisionList=[]
		doesDivide=False
		for x in range(2,5):
			if(x!=number):
				divisionList.append(number%x)

		for t in divisionList:
			#print str(t)
			if t==0:
				doesDivide=True
		return doesDivide

while(notDone):
	if(bigNumber%number==0):
			if(not dividesSomething(number)):
				primeList.append(number)
				bigNumber=bigNumber/number
				print "Breaking down original number down to 1 to generate biggest Prime currently at: " + str(bigNumber)
				number=1
				if(bigNumber==1):
					print str(primeList[-1])
					notDone=False

	

	
	number=number+1





