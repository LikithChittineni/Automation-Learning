#Program that divides two numbers and handles exceptions
a=20
b="abc"
try:
    print("started")
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero...")
except TypeError:
    print("Wrong type...")
except Exception :
    print("something went wrong...")
finally:
    print("ended")

#string to an integer
s="123"
try:
    num=int(s)
    print("Conversion successful:",num)
except ValueError:
    print("Conversion failed")

#accesing a list element using an index
li=[1,2,3]
index=1
try:
    print("Element:",li[index])
except IndexError:
    print("Index out of range! Please try with a valid index")

#File Handling
f_name="sample.txt"
file=None
try:
    file=open(f_name,"r")
    content=file.read()
    print("File Conetent:",content)
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()
        print("File closed")

#function
def divide(a=10,b=11):
    try:
        print(b/a)
    except ZeroDivisionError:
        print("Cannot divide by zero...")
divide(b=20)