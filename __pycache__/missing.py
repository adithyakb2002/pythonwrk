# a=[0,1,2,3,5]
# # b=len(a)
# for i in range(10):
#     if i not in a:
#         print(i)
# letter={2:'abc', 3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
# # comb=[]
# for i in letter:
#     b=int(input('enter ur num'))
#     print()
    
letter={1:'$',2:'abc', 3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz',0:'#'}
b=int(input('enter number'))
if b<=9:
    n1=letter[b]
    for i in n1:
        print(i)

elif b<=9 and b>=100:

 c=b//10
d=b%10
n1=letter[b]
n2=letter[b]
for i in n1 :
    for j in n2:
        print(i+j)
    print(" ")    
