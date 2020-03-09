list=['abcdcba','saiias']
count1=0
for i in range(0,2):
    x=list[i]
    n=len(x)
    count=0
    for j in range(0,int(n/2)):
        if x[i]==x[(n-1)-i]:
            count=count+1
        if count==int(n/2):
            count1=count1+1
print(count1)            
            