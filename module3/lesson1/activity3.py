#take input from the user
rowSize=int(input("enetr the number of rows:"))
if rowSize%2==0:#conditions
    halfDiamRow=int(rowSize/2)
else:
    halfDiamRow=int(rowSize/2)+1
space=halfDiamRow-1
    #loop for the upper part
for i in range(1,halfDiamRow+1):#loop for rows
    for j in range(1,space+1):#loop for coloumns
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
    #incrementing number at each coloumn
        num=num+1
    print()
space = 1
#loop for the lower part
for i in range(1,halfDiamRow):#loop for rows
    for j in range(1,space+1):#loop for coloumns
        print(end=" ")
    space=space+1
    num=1
    for j in range(1,2*(halfDiamRow-i)):
        print(end=str(num))#display result
    #incrementing number at each coloumn
        num=num+1
    print()
                                       