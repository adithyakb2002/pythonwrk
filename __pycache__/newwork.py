print('*VIJAYAMATHA PUBLIC SCHOOL*')
print('*HOTEL MANAGEMENT SYSTEM*')
print('$$$$$$$$$$-HOTEL MARINE VIEW-$$$$$$$$$$')
print()
print()
print()
print()
print('***Designed and Maintained by:')
print('***ANITTA M MATHEW XII A ROLL NO-9[2023-2024]')
print('***DIYA BABU XII A ROLL NO-18[2023-2024]')
print('***ANNA MANESH XII A ROLL NO-10[2023-2024]')
print('***AMALA VARGHESE XII A ROLL NO-7[2023-2024]')
print('***JOANNA LIZ WILSON XII A ROLL NO-22[2023-2024]')
print('***THAFEEQA SAMEEM XII A ROLL NO-38[2023-2024]')
print()
print()

        
          

import pickle
L=[]
price=[]
Price=[]
def booking():
    global L
    print("BOOK YOUR ROOMS")
    a=open("Marine.dat","wb")
 
    L1=[]
    n=int(input("ENTER NUMBER OF ROOMS REQUIRED"))
    for i in range(n):
          name=str(input("ENTER YOUR NAME-"))
          phno=str(input("ENTER YOUR PHONE NUMBER-"))
          addr=str(input("ENTER YOUR ADDRESS-"))
          idn=str(input("ENTER YOUR ID NUMBER-"))
          LI=(name,phno,addr,id)
          L.append(L1)
          pickle.dump(L,a)
    d=input("ENTER DATE IN DD/MM/YYYY")
    a.close()



def room_info():
    global price
    global L
    global Price
    a=open("Marine.dat","wb+")
    room=[]
    l2=[]
    print("1. Standard Non-AC - Rs. 3500")
    print("2. Standard AC - Rs. 4000")
    print("3. 3-Bed Non AC - Rs. 4500")
    print("4. 3-Bed AC - Rs. 5000")
    n=int(input("ENTER NUMBER OF ROOMS"))
    for i in range(n):
        ch=int(input("ENTER YOUR CHOICE"))
        if ch == 1:
            room.append('Standard Non-AC')
            print("Room Type- Standard Non-AC")
            price.append(3500)
            print("Price- 3500")
        elif ch == 2:
            room.append('Standard AC ')
            print("Room Type- Standard AC")
            price.append(4000)
            print("Price- 4000")
        elif ch == 3:
            room.append('3-Bed Non-AC')
            print("Room Type- 3-Bed Non-AC")
            price.append(4500)
            print("Price- 4500")
        elif ch == 4:
            room.append('3-Bed AC')
            print("Room Type- 3-Bed AC")
            price.append(5000)
            print("Price- 5000")
        else:

            print(" Wrong choice..!!")
    l2=[room,price]
    L.append(l2)
    Price.append(price)
    pickle.dump(L,a)
   
    print("")
    print("\t\t\t*ROOM BOOKED SUCCESSFULLY*\n")
    a.close()

def hotel_service():
    global L
    n=(input('ENTER YOUR NAME-'))
    ob=open("Marine.dat","wb+")
    global price
    print('1.RESTAURANT')
    print('2.GAMING')
    y=int(input("Enter your choice-"))
    
    if y==1:
        # f=int(input("Enter your quantity of food-"))
        for i in range(1):
            print('FOOD DRINKS')
            print('------------')
            print('1.Wine .Rs.200')
            print('2.Coffee.Rs.20')
            print('3.Tea.Rs.20')
            print('4.Orange Juice.Rs.50')
            print('5.Mango Juice.Rs.50')
            print('6.Beer.Rs.200')
            print('7.Milkshake.Rs.80')
            print('8.Milk.Rs.15')
            print('9.Water.RS.10')
            print('**')
            print('INDIAN FOOD')
            print('------------')
            print('10.Veg Biriyani.Rs.120')
            print('11.Fish Biriyani.Rs.130')
            print('12.Mutton Biriyani.Rs.145')
            print('13.Chicken Biriyani.Rs.150')
            print('14.Idiyappam.Rs.50')
            print('15.Idli.Rs.40')
            print('16.Omlette.Rs.25')
            print('17.Aloo Tikki.Rs.100')
            print('18.Chola Bhatura.Rs.100')
            print('19.Dhokla.Rs.100')
            print('***')
            print('DESSERTS')
            print('------------')
            print('20.Cakes.Rs.25')
            print('Ice Cream.Rs.25')
            print('23.Brownies.Rs.30')
            print('24.Donuts.Rs.30')
            print('25.Cupcakes.Rs.30')
            print('**')
            f=int(input('Enter your choice of food-'))
            m=int(input('Enter the amount-'))
            s=int(input('Enter no.of peoples have ate-'))
            rf=(s*m)
            r=0+rf
            
            price.append(rf)
            print('your bill is Rs.',rf)
            ch=input('do you want more?,Y/N')
            if ch=='y' or ch=='Y':
                continue
            else:
                print()
                print('YOUR TOTAL BILL IS RS.',r)
                print('HOPE YOUR STOMACH IS HAPPY :)')
                break
    elif y==2:
        g=int(input('How many games do you want to try?'))
        for i in range(g):
            print()
            print()
            print('OUTDOOR GAMES')
            print('--------------')
            print('1.Teniis. per hr=500')
            print('2.Polo. per hr=350')
            print('3.Golf. per hr=750')
            print('4.Badminton. per hr=750')
            g=int(input('Enter your interested game-'))
            mo=int(input('Enter the amount-'))
            h=int(input('How many hours you have played?'))
            rg=(h*mo)
            r=0+rg
          
            price.append(rg)
            print('your payment amount is Rs.',rg)
                
            gam=input('do you want to continue playing?,Y/N')
            
            print()
            print('YOUR TOTAL AMOUNT IS',r) 
            print('HOPE YOU HAD A GOOD TIME')
                
    
    print("THANKYOU FOR USING OUR SERVICES") 
    pickle.dump(price,ob)
    Price.append(price)
    ob.close()
def payment():
    global L
    ob=open("Marine.dat","wb+")
    a='y'
    while a=='y' or a=='Y':
        ph=str(input("Phone Number-"))
        co=str(input("ENTER CHECK-OUT DATE IN DD/MM/YYYY"))
        d=int(input("Enter your total days in Marine View"))
        print("---------PAYMENT----------")
        print("MODE OF PAYMENT")
        print("1-Credit/Debit Card")
        print("2-Using UPI")
        print("3-Cash")
        print("Your Total Bill Is")
        print(sum(Price))
        ch=int(input("Enter Your Mode Of Payment"))
        if ch==1:
            print("PAYING FOR MARINE VIEW")
            print("Pay In The Reception")
            print("THANKYOU")
            print("VISIT AGAIN :)")
        elif ch==2:
            print("PAYING FOR MARINE VIEW")
            print("UPI Number is: 974XXXXXXXX")
            print("If we recieved the payment we will notify you with a message")
            print("THAKYOU")
            print("VISIT AGAIN :)")
        elif ch==3:
            print("PAYING FOR MARINE VIEW")
            print("THANKYOU")
            print("VISIT AGAIN :)")
        else:
            print("INVALID CHOICE FOR PAYMENT MODE")
            cho=input("Do you want to try again? Y/N")
            if cho=="Y" or cho=="y":
                continue
            else:
                break
    print("*****PAYMENT WAS SUCCESSFULL****")
    


def record():
    ob=open('Marine.dat','wb+')
    l=[]
    na=str(input("Enter your Name-"))
    ph=str(input("Enter your phone number-"))
    adr=str(input("Enter your address-"))
    idi=str(input("Enter your Id number"))
    cii=str(input("Enter your Check-In date:"))
    rmn=str(input("Enter your Room NO:"))
    ttl=float(input("Enter your total bill-"))
    coo=str(input("Enter your Check-Out date:"))
    l1=[na,ph,adr,idi,cii,rmn,ttl,coo]
    l.append(l1)
    pickle.dump(l,ob)
    print("YOUR RECORD IS UPDATED SUCCESSFULLY")
    ob.close()

while True:
    print("1. BOOK YOUR ROOMS")
    print("2. ROOMS INFO")
    print("3. SERVICES")
    print("4. PAYMENT")
    print("5. RECORD")
    print("0. EXIT")
    ch=int(input("ENTER YOUR CHOICE"))
    if ch==1:
        print("Book your rooms")
        booking()
    elif ch==2:
        room_info()
    elif ch==3:
        hotel_service()
    elif ch==4:
        payment()
    elif ch==5:
        record()
    elif ch==0:
        break
    else:
        print("INVALID CHOICE")