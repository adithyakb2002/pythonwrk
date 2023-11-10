class Name:
    def myname(adithya):
        print('my name is adithya')
class Name_age(Name):
    def age(adithya):
        print('age is 21')
class Name_fam :
    def fam(adithya):
        print('fam members are 8')         
                                         
class Name_char(Name_age,Name_fam):      
    def char(adithya):                   
        print('good character')          
a=Name_char()                            
a.myname()                               
a.age()  
a.char() 
a.fam()  



