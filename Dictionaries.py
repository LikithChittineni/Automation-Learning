di={'Apple':100,'Orange':50,'Mango':150}
print(di.keys())
print(di.values())
print(di.items())
print(di)
print(di['Apple'])
for key,value in di.items():
    print(f'Cost of {key} is {value}')

file1={111:50,112:60,113:40,114:80}
file2={120:30,121:37}

file1.update(file2)
#print(file1)
#file1.clear()
print(file1)
file1.popitem()
print(file1)
del file1
#simple code of adding a new key-value , popping and updating old key-value.
student = {"name": "Likith", "age": 19, "weight": 51}
print(student["name"])
student["height"]=170
student["age"]=20
print(student)
student.pop("weight")
print(student)
for key,value in student.items():
    print(key,":",value)

top_student=''
max_marks=0
students={"Ram":98,"Shyam":89,"John":90,"Abdul":91,"Wintox":82}
for name,marks in students.items():
    if marks>max_marks:
        max_marks=marks
        top_student=name
print(f"student Name:",top_student,",marks=",marks,)
students["Likith"]=97
print(students)
