# 첫수를 넣으세요    2
# 끝수를 넣으세요    4
# 배수를 넣으세요    3
# 2에서 4까지 3의 배수의 합은 3입니다.

firstNum = int(input("첫수를 넣으시오"))        
lastNum = int(input("끝수를 넣으시오"))
multipleNum = int(input("배수를 넣으시오"))

sum = 0
for i in range(firstNum, lastNum+1):
    if i%multipleNum == 0:
        sum += i 
        
print("{}에서 {}까지 {}의 배수의 합은 {}입니다.".format(firstNum, lastNum, multipleNum, sum))        
            