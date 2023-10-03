# a=int(input('enter the limit'))
# sum=0
# for i in range(10):
#     n=int(input('enter element'))
#     sum+=n
#     print(sum)
a=[1,2,3,3,4,5,6,6,7]
for i in range(10):
   if a.count(i)>1:
     print(i)