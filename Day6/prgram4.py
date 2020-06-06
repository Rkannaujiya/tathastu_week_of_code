n = int(input("enter an integer: "))

temp = n
l=[]
while(temp!=0):
    d = temp%10
    l.append(d)
    temp=temp//10

size = len(l)

x=-1
for k in range(size):
    for i in range(k+1,size):
        if l[i]<l[k]:
            l[i],l[k]=l[k],l[i]
            x=i
            break
    if x!=-1:
        break

if x==-1:
    print("no such number possible")
else:
    l1=l[0:x]
    l1.sort()
    num = l[size-1:x-1:-1] + l1
    print("the next smallest number is:",end=" ")
    for i in range(size):
        print(num[i],end="")
