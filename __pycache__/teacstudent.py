student={}
regno=1001
fee=12000
balance=0
depamount=[]
studentli=[]
teachlist=[]
studentstore=[]
teachstore=[]
stdname=[]
while True:
    print('1.student name','2.teacher','3.viewstudent','4.viewteacher','5.viewasign','6.viewdepasign','7.fee','8.teachstdlist','9.amountpay','10.exit()')
    choice=int(input('enter your choice'))
    if choice==1:
         name=input('enter student name')
         student['name']=name
         age=int(input('enter student age'))
         student['age']=age
         stddepartment=input('enter student department')
         student['stddepartment']=stddepartment
         student["fees"]=fee
         student['regno']=regno
         regno=regno+1
         studentli.append(student.copy())
    if choice==2:
             name=input('enter teacher name')
             teachlist.append(name)
            #  teachdepartment=input('enter  department')
            #  teachlist.append(teachdepartment)
    if choice==3:
            for i in studentli:
             print('-'*20)
             for j ,k in i.items():
                 print(j,':',k)
             print('-'*20)        
    if choice==4:
            for i in teachlist:
             print('-'*20)
             for j ,k in i.items():
                 print(j,':',k)
             print('-'*20)        
    if choice==5:
            student=input('enter student name')
            for i in studentli:
                  studentstore.append(i['name'])
            b=len(teachlist)    
            for j in range(b):  
                  if student in studentstore:
                        for i in studentli:
                              if i['name']==student:
                               i['teachstore']=teachlist[j]
                  # print(studentli)     
            for i in studentli:
             print('-'*20)
             for j ,k in i.items():
                 print(j,':',k)
             print('-'*20)        
    if choice==6:
           student=input('enter department ')
           for i in studentli:
                  studentstore.append(i['stddepartment'])
            # b=len(teachlist)    
            # for j in range(b):  
           if student in studentstore:
              for i in studentli:
                 
                 if i['stddepartment']==student:
                        for n in teachlist:
                               
                               i['teachstore']=teachlist[0]
                 else:
                               i['teachstore']=teachlist[1]
           for i in studentli:
             print('-'*20)
             for j ,k in i.items():
               print(j,':',k)
             print('-'*20)        
    if choice==7: 
           student=input('enter student name')
           for i in studentli:
              studentstore.append(i['name'])
              
              if fee<=12000:
                   
                    amount=int(input('enter your amount'))
                    i["paid"]=amount
              i['fees']=12000-amount
           print(studentli)   
                            
    if choice==8: 
             teacher=input('enter teacher name')
             if teacher in teachlist:
                for i in studentli:
                   if i['teachstore']==teacher:
                           stdname.append(i['name'])
                print(stdname)
    if choice==9: 
           for i in studentli:
              print('name:',i['name'],'paid:',i['paid'],'fees:',i['fees'])     
    if choice==10:                     
          exit()                
