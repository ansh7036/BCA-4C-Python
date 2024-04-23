def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print("Name: Ansh\n Rollno.: 2210997036")
n= int(input("Enter the number: "))
print(f"Factorial of {n} is {fact(n)}")
