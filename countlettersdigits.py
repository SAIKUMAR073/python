s=input("input a string")
c=d=e=0
for i in s:
  if i.isdigit():
    c=c+1
  elif i.isalpha():
    d=d+1
  else:
    e=e+1
print("number of letters:",d)
print("number of digits:",c)
print("number of other characters",e)