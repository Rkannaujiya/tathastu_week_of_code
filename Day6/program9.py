print("enter a list of integers: ",end="")
l = [int(x) for x in input().split()]
k = int(input("enter the value of k: "))

l.sort()

print("the",k,"th smallest integer is:",l[k-1])
