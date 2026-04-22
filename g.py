try:
    print("Enter two numbers")
    a,b=int(input()),int(input())
    c=a/b
    print("Result is",c)
except ZeroDivisonError:
    print("cannot divide by zero")
except ValueError:
    print("Input thikk se likho")
except:
    print("Some Problem")
else:
    print("You are in else block")
finally:
    print("you are in finally block")
print("Enter two numbers")
x,y=int(input()),int(input())
z=x*y
print("product is",z)
