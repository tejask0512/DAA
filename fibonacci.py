n=int(input(" Enter the no of terms you want"))
def fibonacci(n):
     a=0
     b=1
     c=0
     print(a)
     while(c<=n):
          a=b
          b=c
          c=a+b
          print(c)
fibonacci(n)


