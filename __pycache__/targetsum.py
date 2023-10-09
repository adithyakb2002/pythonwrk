root=[8,6,3]
sum1=0
sum2=0
targetsum=10
sum1=(root[0]+root[1])
sum2=(root[0]+root[2])
if targetsum==sum1 or targetsum==sum2:
       print('true')
else:
     print('there is no root to leaf path with targetsum=10')    
