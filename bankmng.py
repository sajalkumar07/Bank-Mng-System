#pylint: disable=unused-variable
from os import system
system('cls')
import mysql.connector
import datetime
now = datetime.datetime.now()
print (now.strftime('Date : '"%d-%m-%Y   \nTime : %H:%M"))
import time
print()

info=mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    charset="utf8",
    database="bank",
)



print('\t\t\t\t ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('\t\t\t\t |                       BADA BANK                           |')
print('\t\t\t\t ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#main function 
def menu():
    print()
    print('1. Open new account')
    print('2. Deposite cash')
    print('3. Withdrawal cash')
    print('4. Update customer detail')
    print('5. Customer detail')
    print('6. Balance inquiry')
    print('7. Close account')
    print('0 to "RETURN"')
    print()

#funtion for opening new account
def opennew():
    
    mycursor = info.cursor()

    fname=input("Candidate's FristName - ")
    sname=input("Candidate's SecondName - ")
    dob=input("Date Of Birth - ")
    add=input("Residential Address - ")
    adhno=input("AadharCard No. - ")
    phno=input("Contact No - ")
    accno=input("Account Number - ")
    cash=input("Opening Ammount - ")
    print()
    
    opt=input('Press Y to save data : ')
    #condition for executing insert command 
    #execute only when user prees y
    if opt=='y':      
    
        sql="insert into accounts values('"+fname+"','"+sname+"','"+dob+"','"+add+"','"+adhno+"',"+phno+",'"+accno+"')"
        sql1="insert into amount values('"+fname+"','"+sname+"','"+accno+"',"+cash+")"
        
        mycursor.execute(sql)
        mycursor.execute(sql1)
        
        #commit method for updateing changes in sql database 
        info.commit()
        info.close()
        
        print()
        print('Saving.....')
        print()
        #time sleep method for some delay 
        time.sleep(5)
        system('cls')
        
        print()
        print('Saved')
        time.sleep(1)
        system('cls')
        print()
        print('press any key to return')
        opt=input('')
        system('cls')
        #if opt=='r':
        menu()
        system('cls')
        print()

#Cash deposite Function 
def depo():

    info=mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    charset="utf8",
    database="bank",
    )

    mycursor = info.cursor()

    accno=input('Acount number : ')
    amt=input('Deposite Amount : ')

    mycursor.execute("select balance from amount where accountnumber='"+accno+"'")
    myresult=mycursor.fetchall()

    print()
    print('Please Wait....')
    time.sleep(3)
    system('cls')
    print()

    sql="update amount set balance=balance+'"+amt+"' where accountnumber='"+accno+"'"
    mycursor.execute(sql)
    info.commit()
    info.close()
    print("Amount Credited to Account :'"+accno+"'")
    print()
    print('press any key to return')
    opt=input('')
    system('cls')
    #if opt=='r':
    menu()
    system('cls')
    print()

#cash withdrawal function 
def withdrawl():

    info=mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    charset="utf8",
    database="bank",
    )

    mycursor = info.cursor()

    accno=input('Acount number : ')
    amt=input('Withdrawal Amount : ')

    mycursor.execute("select balance from amount where accountnumber='"+accno+"'")
    myresult=mycursor.fetchall()

    print()
    print('Please Wait....')
    time.sleep(3)
    system('cls')
    print()

    sql="update amount set balance=balance-'"+amt+"' where accountnumber='"+accno+"'"
    mycursor.execute(sql)
    info.commit()
    info.close()
    print("Amount Ddebited From Account : '"+accno+"'")

    print('press any key to return')
    opt=input('')
    system('cls')
    #if opt=='r':
    menu()
    system('cls')
    print()

#update function declaretion    
def update():

    info=mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    charset="utf8",
    database="bank",
    )

    mycursor=info.cursor()
    
    accno=input('Enter account number : ')
    print()
    mycursor.execute("select firstname,secondname,contactno,residentialaddress from accounts where accountnumber='"+accno+"'")
    myresult=mycursor.fetchall()

    system('cls')

    for x in myresult:   
        print("FristName - ",x[0])
        print("SecondName - ",x[1])
        print("Residential Address - ",x[2])
        print("Contact No - ",x[3])
        print()
    

        print('a. Update Name')
        print('b. Update Residential Address')
        print('c. Update Contact Number')
        print()                                                                             

        opt=input('Enter a,b,c according changes :')
        print()
        
        if opt=='a':
            fname=input('Enter New Frist Name : ')
            sname=input('Enter New Second Name : ')
            sql=("update accounts set secondname='"+sname+"' where accountnumber='"+accno+"'" )
            sql1=("update amount set secondname='"+sname+"' where accountnumber='"+accno+"'" )
            mycursor.execute(sql)
            mycursor.execute(sql1)
            info.commit()
            info.close()
            print()
            print('Changes Done')
            
            print()
            print('Prees u to return on update menu')
            print('Prees r to return on main menu')    
            print()
            
            opt=input('Enter your choice here : ')

            if opt=="u":
                update()
            elif opt=="r": 
                menu()
                system('cls')
    
        
        elif opt=='b':
            add=input('Enter new address : ')
            sql=("update accounts set residentialaddress='"+add+"' where accountnumber='"+accno+"'")
            mycursor.execute(sql)
            info.commit()
            info.close()
            print()
            print('Changes Done')

            print()
            print('Prees u to return on update menu')
            print('Prees r to return on main menu')    
            print()
            
            opt=input('Enter your choice here : ')

            if opt=="u":
                update()
            elif opt=="r":
                menu()
                system('cls')
    
        
        elif opt=='c':
            phno=input('Enter new Contact Number : ')
            sql=("update accounts set contactno='"+phno+"' where accountnumber='"+accno+"'")
            mycursor.execute(sql)
            info.commit()
            info.close()
            print()
            print('Changes Done')

            print()
            print('Prees u to return on update menu')
            print('Prees r to return on main menu')    
            print()
            
            opt=input('Enter your choice here : ')

            if opt=="u":
                update()
            elif opt=="r":
                menu()
                system('cls')

#Customer detail function   
def detail():

    info=mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    charset="utf8",
    database="bank",
    )
    
    mycursor=info.cursor()

    accno=input('Enter Account Number : ')
    print()
    print('Preparing Customer Data....')
    print()
    time.sleep(5)
    mycursor.execute("select * from accounts where accountnumber='"+accno+"'")
    myresult=mycursor.fetchall()

    for x in myresult:   
        print("FristName - ",x[0])
        print("SecondName - ",x[1])
        print("Date Of Birth - ",x[2])
        print("Permanent Address - ",x[3])
        print("AadharCard No. - ",x[4])
        print("Contact No - ",x[5])
        print("Account Number - ",x[6])
        print()

        print('press any key to return')
        opt=input('')
        system('cls')
        #if opt=='r':
        menu()
        system('cls')
        print()

#Customer's Balace Funtion
def baliq():

    info=mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    charset="utf8",
    database="bank",
    )
    
    mycursor=info.cursor()

    accno=input('Enter account number : ')
    print()

    print()
    print('Please wait....')
    print()
    time.sleep(5)
    
    mycursor.execute("select firstname,secondname,accountnumber,balance from amount where accountnumber='"+accno+"'")
    myresult=mycursor.fetchall()
    system('cls')

    for x in myresult:
        print('First Name : ',x[0])
        print('second Name : ',x[1])
        print('Account number - ',x[2])
        print('Remaning balance - ',x[3])
        print()
        print('press any key to return')
        opt=input('')
        system('cls')
        #if opt=='r':
        menu()
        system('cls')
        print()

#function to completely delete Customer's 
def close():

    info=mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    charset="utf8",
    database="bank",
    )
    
    mycursor=info.cursor()

    accno=input('Enter account number : ')
    print()
    print("Preparing Customer's Data....")
    time.sleep(5)
    mycursor.execute("select * from accounts where accountnumber='"+accno+"'")
    myresult=mycursor.fetchall()
    system('cls')

    for x in myresult:   
        print("FristName - ",x[0])
        print("SecondName - ",x[1])
        print("Date Of Birth - ",x[2])
        print("Permanent Address - ",x[3])
        print("AadharCard No. - ",x[4])
        print("Contact No - ",x[5])
        print("Account Number - ",x[6])
        print()

        opt=input('Do you want to peremanently close this account Y/N : ')
        if opt=="y":
            print()
            print('Closing.....')
            time.sleep(5)
            print('')
            sql="delete from accounts where accountnumber='"+accno+"'"
            sql1="delete from amount where accountnumber='"+accno+"'" 
            mycursor.execute(sql)
            mycursor.execute(sql1)
            info.commit()
            info.close()
            system('cls')
            print()
            print('Your account has permanently closed')
            print()
            print('Thank You')
            print()

            print('press any key to return')
            opt=input('')
            system('cls')
            #if opt=='r':
            menu()
            system('cls')
            print()


        elif opt=="n":
            print()
            print('Right decision')
            print()
            time.sleep(1)
            system('cls')
            print('press any key to return')
            opt=input('')
            system('cls')
            #if opt=='r':
            menu()
            system('cls')
            print()

while True:
    print()
    print('==========================================================')
    print('|    1. Open new account                                 |')
    print('|    2. Deposite cash                                    |')
    print('|    3. Withdrawal cash                                  |')
    print('|    4. Update customer detail                           |')
    print('|    5. Customer detail                                  |')
    print('|    6. Balance inquiry                                  |')
    print('|    7. Close account                                    |')
    print('|    0 to "RETURN"                                       |')
    print('==========================================================')
    print()
    choice=int(input('     Enter your choice - '))
    print()

    if choice==1:
        system('cls')
        print()
        print('==================Opening New Account==================')
        print('===================Enter Your Detail===================')
        print()
        opennew()
    elif choice==2:
        system('cls')
        print()
        print('==================Deposite Cash==================')
        print('=========Please Enter Your Account Number========')
        print()
        depo()
    elif choice==3:
        system('cls')
        print()
        print('==================Withdrawl Cash==================')
        print('=========Please Enter Your Account Number=========')
        print()
        withdrawl()
    elif choice==4:
        system('cls')
        print()
        print('==================Update Youre Details==================')
        print('============Please Enter Your Account Number============')
        print()
        update()
    elif choice==5:
        system('cls')
        print()
        print('==================Check Account Detail===================')
        print('=============Please Enter Your Account Number============')
        print()
        detail()
    elif choice==6:
        system('cls')
        print()
        print('==================Account Balance Inquairy==================')
        print('==============Please Enter Your Account Number==============')
        print()
        baliq()
    elif choice==7:
        system('cls')
        print()
        print('==================Close Bank Account==================')
        print('===========Please Enter Your Account Number===========')
        print()
        close()
    elif choice==0:
        system('cls')
        print()
        print('\t\tpress X to exit')
        print('\tprees M to return on main menu')
        print()
        
        opt=input('Enter your choice here : ')

        if opt=='x':
            system('cls')
            break
        elif opt=='m':
            menu()
            system('cls')


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 