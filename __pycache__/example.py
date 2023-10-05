# a=[3,2,4]        
# b=[]
# target=6
# if a[0]+a[1]==target:
#         b.append(0)
#         b.append(1)
#         print(b)
# elif a[1]+a[2]==target:
#         b.append(1)
#         b.append(2)
#         print(b)
# elif a[0]+a[2]==target:
#         b.append(0) 
#         b.append(2)
#         print(b)  

a=[2,4,7,6]
target=10
b=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
            b.append(i)
            b.append(j)
            print(b)


