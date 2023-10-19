student={}
regno=1001
studentli=[]
teacher={}
teachlist=[]
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
          teacher['teachername']=teachername
          teachdepartment=input('enter teaching department')
          teacher['teachdepartment']=teachdepartment
          teachlist.append(teacher.copy())
    if choice==4:
              for i in teachlist:
                    print('-'*20)
                    for j,k in i.items():
                       print(j ,':', k)
              for i in teachlist:
                    print('-'*20)
    if choice==5:
          exit()                
