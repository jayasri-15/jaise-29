#class and object

class Student:
    name=""
    rollno=0
s=Student()             #create obj
s.name="jayasri"
s.rollno=23
print(s.name,s.rollno)
class Sample:
    name=""
    rollno=0
b=Sample()           # create obj          #
b.name="sam"
b.rollno=51
print(b.name,b.rollno)

class Jayasri:
    x=23
k=Jayasri()
print(k.x)

#defining a method
class MyClass:
    pass
    def asd(self):
        print("hai How are u jaya")
m=MyClass()            #create obj
m.asd()                #callinf func