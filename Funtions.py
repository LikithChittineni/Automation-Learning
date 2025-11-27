#Grades
def Grade(score):
    if score>90:
        return "A"
    elif score>75 and score<90:
        return "B"
    else:
        return"C"
c=Grade(8)
print(c)


#max of three numbers
def Find_max(a,b,c):
    if a>b and a>c:
        print("Max is A:",a)
    elif b>a and b>c:
        print("Max is B:",b)
    else:
        print("Max is C:",c)
Find_max(10,20,15)


#Even numbers only
def Even(OriginalList: List[int])->Optional[List[int]]: #optional list here specifies that op may be list[int] or None
    even=[]
    for i in OriginalList:
        if i%2==0:
            even.append(i)
    if even==[]:
        return None
    return even

example1=[10,1,4,5,9.63]
example2=[1,3,5,7,9]

print("original List1:",example1)
print("Even Numbers List1:",Even(example1))

print("original List2:",example2)
print("Even Numbers List2:",Even(example2))


