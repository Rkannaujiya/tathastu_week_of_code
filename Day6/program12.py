print("enter an array of strings: ")
l = [x for x in input().split()]

l.sort(reverse=True,key=len)

pre = l[0]

for i in range(1,len(l)):
    x = len(l[i])
    for j in range(len(l[i])):
        if j==len(pre):
            x=len(pre)
            break
        if l[i][j]!=pre[j]:
            x=i
            break
    pre = pre[0:x]

print("the longest common prefix is: ",pre)
