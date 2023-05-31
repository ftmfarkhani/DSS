#receive input from user
text=input("please enter a text:")
LetterCountDict={}

for l in text:
    #check if letter is alphabet 
    if l !=" ":
        if l in LetterCountDict:
            LetterCountDict[l]+=1
        else:
            LetterCountDict[l]=1  

#print table
print("\n+-------+------------+")
print("| Name  |  Frequency |")
print("+=======+============+")
for i in LetterCountDict:
    print ("|",i,"    |         ",LetterCountDict[i],"|")        
    print("+-------+------------+")