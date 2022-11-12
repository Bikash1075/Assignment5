# Complete Student Class
class Student:
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self,rollno):
        self.__rollno=rollno
    def getRollNumber(self):
        return self.__rollno
s=Student()
s.setName("Bikash")
print(s.getName())
s.setRollNumber(75)
print(s.getRollNumber())
