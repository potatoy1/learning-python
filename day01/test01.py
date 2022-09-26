# 1~100까지의 정수 중 3의 배수의 합을 구하시오
a = range(1,101)
sum = 0


for i in a:
    if i%3 == 0 :
       sum += i
print(sum)
