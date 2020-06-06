i=input()
l=len(i)
for x in range (0,l):
	t=i[:l-x];
	r=t[::-1];
	if(t==r):
		print(l-len(r));
		break;
