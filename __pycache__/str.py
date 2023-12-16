a=input('enter string')
a=a.split(' ')
b=[]
for i in a:
    b.append(len(i))
print(max(b))
print(a[:1])