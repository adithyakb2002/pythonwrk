student={}
regno=1001
studentli=[]
teachlist=[]
studentstore=[]
teachstore=[]
while True:
    print('1.student name','2.teacher','3.viewstudent','4.viewteacher','5.viewasign','6.exit()')
    choice=int(input('enter your choice'))
    if choice==1:
         name=input('enter student name')
         student['name']=name
         age=int(input('enter student age'))
         student['age']=age
         stddepartment=input('enter student department')
         student['stddepartment']=stddepartment
         student['regno']=regno
         regno=regno+1
         studentli.append(student.copy())
    if choice==2:
             name=input('enter teacher name')
             teachlist.append(name)
            #  teachdepartment=input('enter  department')
            #  teachlist.append(teachdepartment)

    if choice==3:
             print(studentli)
    if choice==4:
             print(teachlist)
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
                  print(studentli)        
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
           print(studentli)        
   
       

    if choice==7:            
          exit()                
