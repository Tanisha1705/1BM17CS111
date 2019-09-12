class student :
    def __init__(self):
        self.__id=None
        self.__age=None
        self.__marks=None

    def validatemarks(self):
        if (self.__marks>65 and self.__marks<100):
            return True
        else:
            return False

    def validateage(self):
        if(self.__age>=20):
            return True
        else:
            return False

    def check_qualification(self):
        m=self.validatemarks()
        a=self.validateage()
        if(m==True and a==True):
            if (self.__marks>65):
                
                 return True
            else :
                 return False
          
        else:
            return False

    def setter(self):
         
         self.__marks=int(input("enter your marks"))
         self.__age=int(input("enter your age"))
         self.__id=int(input("enter youur id"))
    def getter(self):
         print("Student ID= ",self.__id )
         print("Student age =",self.__age)
         print("student marks= ",self.__marks)
         if (self.check_qualification()== True):
             print("qualified")

         else:
             print(" not qualified")


s=student()
s.setter()
s.getter()
    
        
        
