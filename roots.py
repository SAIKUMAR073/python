import math
a=int(input('enter the value of a where (a!=0)'))
b=int(input('enter the value of b'))
c=int(input('enter the value of c'))
print("the quadratic equation is %dx2+%dx+%d"%(a,b,c))
d=((b*b)-(4*a*c))
if d>0:
    print("real roots exits")
    print("the roots are")
    x1=((-b+math.sqrt(d))/(2*a))
    x2=((-b-math.sqrt(d))/(2*a))
    print("x1=",x1)
    print("x2=",x2)
elif d==0:
    print("equal roots exits")
    print("the roots are")
    x1=((-b)/(2*a))
    x2=((-b)/(2*a))
    print("x1=",x1)
    print("x2=",x2)
else:
    print("complex roots exits")
    print("the roots are")
    t1=((-b)/(2*a))
    t2=((math.sqrt(-d))/(2*a))
    print("x1=%d+%dj"%(t1,t2))
    print("x2=%d-%dj"%(t1,t2))
    
    
    
    