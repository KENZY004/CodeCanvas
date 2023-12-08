def squares(x):
    return x*x
def double(x):
    return 2*x
num=int(input("num: "))
result=squares(double(num))
print("double,squaring the value:",result)