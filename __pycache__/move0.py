a=[0,1,0,4,9]

for i in a:
    if i==0:
        a.remove(i)
        a.append(i)
print(a)