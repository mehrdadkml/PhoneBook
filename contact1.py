
import group
import typee
import address



class contact1 :
    def __init__ (self) :
        self.name = "mehrdad "
        self.family = "kamali"
        self.number =[]
        self.group=group.group.family
        self.type=typee.typee.home
        self.address=address.address()
        self.email="mehrdadkamalihm@gmail.com"

        
    def displayInfo(self):
        result = ""
        result = result +"\n----- info of contact -----"
        result = result +"\nname of contact= "+ self.name
        result = result +"\nfamily of contact= "+ self.family
        result = result +"\ngroup of contact= "+ self.group.name
        result = result +"\ntype of number= "+ self.type.name
        for i in self.number:
            result=result+("\nnumber of contact= "+str(i))

        #result = result +"\nnumber of contact= "+ str(self.number)
        result = result +"\naddress of contact= "+ self.address.displayaddress()  
        result=result+"\naddress of contact= "+ self.email   
        return result




