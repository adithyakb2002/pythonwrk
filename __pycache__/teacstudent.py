student={}
regno=1001
studentli=[]
# teacher={}
teachlist=[]
studentstore=[]
teachstore=[]
while True:
    print('1.student name','2.viewstudent','3.teachers','4.viewteacher','exit()')
    choice=int(input('enter your choice'))
    if choice==1:
         stdname=input('enter student name')
         student['stdname']=stdname
         stdage=int(input('enter student age'))
         student['stdage']=stdage
         stddepartment=input('enter student department')
         student['stddepartment']=stddepartment
         student['regno']=regno
         regno=regno+1
         studentli.append(student.copy())
    if choice==2:
              for i in studentli:
                    print('-'*20)
                    for j,k in i.items():
                       print(j ,':', k)
              for i in studentli:
                    print('-'*20)

    if choice==3:
          teachername=input('enter teacher name')
          student['teachername']=teachername
          teachdepartment=input('enter teaching department')
          student['teachdepartment']=teachdepartment
          teachlist.append(student.copy())
    if choice==4:
            stdname=input('enter student name')
            for i in studentli:
                  studentstore.append(i['stdname'])
   
            if stdname in studentstore:
                  for i in studentli:
                        if i['stdname']==stdname:
                              for j in teachlist:
                                    i['teachlist']=j
                              print(studentli)      
          
            #  for i in studentli:
            #             if i['stdname']==stdname:
            #                   for j in stdname:
            #                       i['teachlist']=j
            #  print(studentli)      

          
    if choice==6:
                
          exit()                
