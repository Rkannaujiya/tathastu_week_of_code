print("enter the list of integers: ",end="")
l = [x for x in input().split()]

for i in range(len(l)):
    a = float(l[i])
    for j in range(i+1,len(l)):
        b = float(l[j])
        for k in range(j+1,len(l)):
            c = float(l[k])
            if ((a+b+c)>1 and (a+b+c)<2):
                print("triplet exists: a=",a,"b=",b,"c=",c,"\ta+b+c=",(a+b+c))
