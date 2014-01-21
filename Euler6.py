import math
bigSum=0
smallSum=0
for x in range(0,101):
	bigSum=bigSum+x
	smallSum=smallSum+math.pow(x,2)

print "result: " + str(math.pow(bigSum,2)-smallSum)