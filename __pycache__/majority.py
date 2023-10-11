a=[1,2,2,2,2,1,2,4,5,2]
b=len(a)
for i in range(b):
    if a.count(i)>b/2:
          print('the majority element is',i)