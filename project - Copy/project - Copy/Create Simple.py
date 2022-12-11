class Student:
name=None
age=0
def display(self,n,a):
self.name=n
self.age=a
print(self.name,self.age)

ob1=Student()
ob1.display("neha",14)
ob2=Student()
ob2.display("Rahul",23)