

numberLine:: (Enum a ,Num a)=> a->a->[a]
numberLine start end = [start,start+1..end]

isEven n = if( (n `mod` 2) == 0)
				then True
				else False

generateEvens (x:xs) = if(isEven x)
							then generateEvens xs
							else x:(generateEvens xs)
generateEvens [] = []

getNumberPrime :: (Integral a)=> [a]->a->a->a
getNumberPrime (x:xs) primeNumberIndex currentPrime = if( (x `mod` 3)==0 || (x `mod` 5)==0 || (x `mod` 7)==0 )
														then (getNumberPrime xs primeNumberIndex currentPrime)
														else (getNumberPrime xs (primeNumberIndex-1) x)
getNumberPrime [] _ _ = error "Not found in domain"
getNumberPrime (x:xs) 0 currentPrime = currentPrime