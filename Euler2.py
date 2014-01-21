##sum of all even fib numbers in sequence

pn=1
pn1=2
sum=0

while(pn<4000000 and pn1<4000000):
	if(pn1%2==0):
		sum=sum+pn1
	maintainpn1=pn1
	pn1=pn+pn1
	pn=maintainpn1

print str(sum)