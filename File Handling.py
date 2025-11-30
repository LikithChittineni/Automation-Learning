f = open("notes.txt", "r")
content = f.read()
print(content)
f.close()

f = open("notes.txt", "r")
words = f.read().split()
print(len(words))
f.close()

f = open("output.txt", "w")
f.write("Day 4 practice done \n")
f.close()

f = open("output.txt", "a")
f.write("Extra line added.\n")
f.close()

print("File handling done.")
