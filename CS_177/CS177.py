from pathlib import Path
'''
with open("sample.txt","r")as csv:
    text=csv.read()
    print(text)
    print('----------')

with open("sample.txt",'r') as csv:
    text=csv.read(5)#reads 5 characters only. Cursor stops at the 6th charater
    print(text)
    line1=csv.readline()#continues from the cursor's position to untill it find \n
    print(line1)
    line2=csv.readline(8)#8 characters from the cursor
    print(line2)
    linen=csv.readlines()#gives a list from the curser where every element is a line
    print(linen)
print("\n---------------------\n")
with open("sample.txt",'r') as csv:
    for i in csv:
        print(i,end='')

#append mode 'a' adds at the end of the file. The pointer starts from the end of the file 
with open("sample_write.txt", "a") as csv:
    csv.write("\n\n")#f.write only writes in the same line, doesn't matter if used multiple f.write() statements
    csv.write("Text is being\n\n  written\n")#use \n to write in a new line.

'''
#r+ mode can read and write in a file that must exist. 
#It starts writing from the pointer location, hence, if the pointer is at the beginning and if we write n no of characters then it replaces first n characters in the file with what we intend to write
with open("sample_write.txt",'r+') as csv:
    csv.write("Hii")
    csv.write('You are studying CS177')

with open("sample_test.txt",'w+') as csv:
    
    csv.write("(Overwritting\nThe lines from here)")
    csv.seek(0)
    text=csv.read()
    print(text)

def appendleft(l,x):
    l=l[::-1]
    l.append(x)
    l=l[::-1]
    return l
def popleft(l):
    l.pop(0)
    return l