def fibborec(n):
    if n<=1:
        return n
    else:
        return fibborec(n-1)+fibborec(n-2)

n=int(input("Enter the no of Terms you want: "))
if n<=0:
    print("Please enter +Ve no")
else:
    for i in range(n):
        print(fibborec(i))