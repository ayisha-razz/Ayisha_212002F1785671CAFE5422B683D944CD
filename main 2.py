def recurfact(n):
 if n==0 or n==1:
   return 1
 else:
   return n*recurfact(n-1)
number=int(input("Enter the number: "))
res=recurfact(number)
print("The factorial of",number,"is",res)