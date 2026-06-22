class Student:
    def __init__(self,name,branch,rollno):
        self.Sname=name
        self.Sbranch=branch
        self.Srollno=rollno
    def name(self):
        print(self.Sname)
    
    def __repr__(self):
          return f"{self.Sname},{self.Sbranch},{self.Srollno}"
    #def __str__(self):
           # return "i am str() dunder method"
s1=Student("x","csm","14")
s2=Student("y","cse","16")
s3=Student("z","csd","12")
print(s1.Sname,s1.Sbranch,s1.Srollno)
print(s2.Sname,s2.Sbranch,s2.Srollno)
print(s3.Sname,s3.Sbranch,s3.Srollno)
#print(s1.name())
print(s1)
print(s2)
str1="hello"
str2="hello"
print((str1))
print((str2))
print(1+2)
print(int. __add__(1,2))
print("1"+"2")
print(str.__add__("1","2"))

