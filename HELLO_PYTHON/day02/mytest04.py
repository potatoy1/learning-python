# 홀/짝을 입력하시오    홀
# 나: 홀
# 컴: 홀
# 결과: 승리 패배
from random import random

player = input("홀/짝을 입력하시오")
computer=""
result=""


computer = random()

if computer > 0.5:
    computer="홀"
else:
    computer="짝"

if player == computer:
    result ="승리"
else :
    result ="패배"

print("player",player)   
print("computer",computer)   
print("result",result)   
       
        