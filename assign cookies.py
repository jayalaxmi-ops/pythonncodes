g=[1,3,3,4,5]
s=[1,1,2,3,4]
g.sort()
s.sort()
i=0
j=0
while(i<len(g) and j<len(s)):
    if(s[j]>g[i]):
        i+=1
    j+=1
print(i)
