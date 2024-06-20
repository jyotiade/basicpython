#====================================================theory=============================================================

# comment in python

# is used for single line comment
'''
this is used for multiple line comment
'''

#=========standard output(it show in console)function f()  ---->print()
#=========standard input(keyboard)
#======python is case sensitive langauage
'''
by default it give new line ,it donot use endl and /n like c++

difference between argument and parameter is argument contain value and parameter contain variable having value

"\n" is used for new line but donot use "endl"
'''

#end parameter in print() ois used to merge different lines in single line  (have to pass string)

#dynamic p.l means the variables datatype donot has to be defined




#===================================================== code =================================================================================================

print("welcome",end=" ")  #bydefault--->newline
print("to",end=" ")
print("python","classes")  #','-->one space preserve

print("today is holiday")


print("hello") # argument or value passing

a="today"
b="is "
c="holiday"
print(a,b,c)  # parameters passing

#===========================================================VARIABLE AND DATATYPE======================================================================
                                                                                                 
'''
VARIABLE-->it is a reference to a  memory area where our data is reside

in python there are two types of memory
1)stack   2)heap     code

   n1        9        instrution
   n2        10
   n3        9

   in this, variable or reference are save in stack and object or data save in heap.
   memory wastage reduce,memory management is good

   if the reference of stack element in first it is different and same element value is different in another entry then second value is taken and used.

   reference behave like pointer
'''
# id() is used to print the address of value ,data or object stored in heap.

n1=9
n2=10
n3=9

print("n1 variable value-->",n1,"n1 address",id(n1))
print("n2 variable value-->",n2,"n2 address",id(n2))
print("n3 variable value-->",n3,"n3 address",id(n3))

# 10---------->de reference (donot used in upcoming code)---->destroyed by gc()
# gc is method which is use to destroy de reference object called by inplicite interpretator
#also konwn sa garbagecollector()
#implicite calling

n2=900

#====
'''
DATYATYPE-->           types
                   

                                                                   (from 1 value map
                                                                        multiple
                                                                     value of its)
                                                                     
        numerals                     sequence                        mapping                set                   none

        int                           list                         dictionary               set                   donot have value ,it is like void
        float                         tuple
        complex(3+4j)                 string
        boolean(true/false)
'''

#Example2:
'''
a=90
b=65
c=50
d=90
c=100

note:here as we see object 50 become dereference,and this value is deleted by method gc(), hence garbagecollector method release memory.

'''
# type() function is used to find the datatype of data ,variable or object


print(type(3))
print(type(45.7))
print(type("happy"))
print(type ([2,3,4]))



















