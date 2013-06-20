# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def not_adjacent_floor(f1, f2):
	"Returns if the two floors are adjacent to each other"
	return not(abs(f1 - f2) == 1)

def higher_floor(f1, f2):
	"Returns if f1 is higher than f2"
	return f1 - f2 > 0

def floor_puzzle():
    floors = [1,2,3,4,5]
    orderings = list(itertools.permutations(floors))
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
    	for [Hopper, Kay, Liskov, Perlis, Ritchie] in orderings
    	if Hopper != 5 and Kay != 1 and higher_floor(Perlis, Kay) and not_adjacent_floor(Ritchie, Liskov) and not_adjacent_floor(Liskov,Kay) and Liskov != 1 and Liskov != 5)