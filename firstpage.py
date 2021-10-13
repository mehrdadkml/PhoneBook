import address
import typee
import group
import contact1

phoneBook=[]
nrr=[]
def Mehrdad():
        Mehrdad=contact1.contact1()
        Mehrdad.name="Mehrdad"
        Mehrdad.family="kamali"
        Mehrdad.number=[4512]
        Mehrdad.email="Mehrdadkml@"
        Mehrdad.address.street="ddfdf"
        Mehrdad.address.avenue="sdsdds"
        Mehrdad.address.pelak=45
        Mehrdad.group =group.group(2)
        Mehrdad.type=typee.typee(1)
        phoneBook.append(Mehrdad)

def behzad():
        Mehrdad=contact1.contact1()
        Mehrdad.name="behiiiii"
        Mehrdad.family="kamali"
        Mehrdad.number=[4512]
        Mehrdad.email="Mehrdadkml@"
        Mehrdad.address.street="ddfdf"
        Mehrdad.address.avenue="fgfg"
        Mehrdad.address.pelak=45
        Mehrdad.group =group.group(2)
        Mehrdad.type=typee.typee(1)
        phoneBook.append(Mehrdad)
        
       

def Hoda():
        Mehrdad=contact1.contact1()
        Mehrdad.name="hodaaaaaaaaaaaaaaa"
        Mehrdad.family="honeyyyyyyyy"
        Mehrdad.number=[4512]
        Mehrdad.email="Mehrdadkml@"
        Mehrdad.address.street="ddfdf"
        Mehrdad.address.avenue="sdsdds"
        Mehrdad.address.pelak=45
        Mehrdad.group =group.group(2)
        Mehrdad.type=typee.typee(1)
        phoneBook.append(Mehrdad)
def ShowGroup():
    a =1
    for i in group.group:
        print(f"{a} ) {i}")
        a=a+1

def ShowType():
    a =1
    for i in typee.typee:
        print(f"{a} ) {i}")
        a=a+1

def displaymenu():

    print("1.add contact    ")
    print("2.remove contact    ")
    print("3.edit contact    ")
    print("4.show all contact    ")
    print("5.search contact by name    ")
    print("6.search contact by phone number  ")
    print("7.exit    ")
enter=-1
Mehrdad()
behzad()
Hoda()    
while (enter!="7")  : 

    displaymenu()

    enter=input("enter your choice:")
    if enter=="1" :
        x=contact1.contact1()
        x.name=input("enter your first name: ")
        x.family=input("enter your last name: ")
        #x.number=int(input("enter your number:"))

        
        e=1
        
        e=input("do you want add another number? yes/no \n")
        while(e=="yes"):
             num=int(input("enter your number: "))
             e=input("do you want add another number? yes/no :\n")
             x.number.append(num)
              


       
        
        x.email=input("enter email:")
        x.address.street=input("enter your street: ")
        x.address.avenue=input("enter your avenue: ")
        x.address.pelak=int(input("enter your pelak: ")) 
        ShowGroup()
        p=int(input("Enter group ? "))
        x.group =group.group(p)
        ShowType()
        p=int(input("Enter type ? "))
        x.type=typee.typee(p)
        phoneBook.append(x)




        


        print("you choose one.")
    if enter=="2" :
        r=input("enter your contact name and delete it: ")
        for i in phoneBook:

            if r==i.name:
                  phoneBook.remove(i)
                  print(f"this contact is removed{i.displayInfo()}")

               


      
       
    if enter=="3" :
        
        name=input("enter your contact's name and edit that: ")
        for i in phoneBook:
            if name==i.name:
                i=contact1.contact1()
                i.name=input("enter your first name: ")
                i.family=input("enter your last name: ")
                i.number=int(input("enter your number:"))
                i.email=input("enter email:")
                i.address.street=input("enter your street: ")
                i.address.avenue=input("enter your avenue: ")
                i.address.pelak=int(input("enter your pelak: ")) 
                ShowGroup()
                p=int(input("Enter group ? "))
                i.group =group.group(p)
                ShowType()
                p=int(input("Enter type ? "))
                i.type=typee.typee(p)
                phoneBook.append(i)
                print(i.displayInfo())

    if enter=="4" :
        print(f"your contacts.{len(phoneBook)}")
        for i in phoneBook:
            print(i.displayInfo())

    if enter=="5" :
        s=input("enter your search contact: ")

        for i in phoneBook:

            if s==i.name:
               print(i.displayInfo())
            else:
                 print("not here")   

        
    if enter=="6" :
        n=int(input("enter your search number"))
        for i in phoneBook:
            if n==i.number:
                print(i.displayInfo())
        print("you choice six.")
    if enter=="7" :
        print("you choice seven.") 


b1=phonebook.phoneBook()

print(b1.displayInfo())
