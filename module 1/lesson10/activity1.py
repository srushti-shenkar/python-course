#input an integer value
n=int(input("enter the number whose sum you want to find"))
sum=0

#iterates for n+1 times: i=1 to n+1
for i in range(1,n+1):
    sum=sum+i
print("\nSum=",sum)
