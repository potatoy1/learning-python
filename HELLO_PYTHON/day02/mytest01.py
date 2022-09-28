# 첫 수를 넣으세요    2
# 끝 수를 넣으세요    4
# 2에서 4까지의 합은 9입니다.

a = int(input("첫 수를 넣으세요"))
b = int(input("끝 수를 넣으세요"))


sum = 0
for i in range(a,b+1):
        sum +=i
# print(a,"에서" ,b ,"까지의 합은",sum,"입니다.")
print("{}에서 {}까지의 합은 {}입니다.".format(a,b,sum))