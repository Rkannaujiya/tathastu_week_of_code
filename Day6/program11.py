print("enter a list of integers: ",end="")
l = [int(x) for x in input().split()]

l.sort()

prod = max( l[0]*l[1]*l[-1] , l[-1]*l[-2]*l[-3] )

print("the highest product is: ",prod)
