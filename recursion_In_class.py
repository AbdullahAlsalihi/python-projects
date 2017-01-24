def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)
    
print(fac(10))

def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
print(reverse('hello'))

# Plandrome 
# 'abcba' return True. if first element doesnot equal last return wrong 
# other wise return True.
# 'abcd' return False

def palidrome(s):
    if len(s) == 0:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        print(s)
        return palidrome(s[1:-1])
print(palidrome('helloolleh'))

# Fib(n) = n-1

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
name = input('enter something: ')
result = fib(int(name))
print('fib(%s) = %d' % (name, result))

import turtle
def draw (myturtle, linelen):
    if linelen > 0:
        myturtle.forward(linelen)
        myturtle.right(90)
        draw(myturtle, linelen - 5)
myturtle = turtle.Turtle()
mywin = turtle.Screen()
draw(myturtle, 150)
mywin.exitonclick()

