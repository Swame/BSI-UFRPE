def f(n):
    if n==0:
        return 0
    return f(n-1)+1
print (f(5))
