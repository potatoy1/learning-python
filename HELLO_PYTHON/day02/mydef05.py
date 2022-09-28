def addminmuldiv(a,b):      # 멀티리턴
    return a+b,a-b,a*b,a/b

sum,min,mul,div = addminmuldiv(4, 6)

print("sum",sum)
print("min",min)
print("mul",mul)
print("div",div)