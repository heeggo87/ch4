temp = ('bird', 'cat', 'dog')

# 변수 여러개 = 튜플
# 튜플의 요소가 순차적으로 변수에 저장됨
b, c, d = temp
print(b, c, d) #bird cat dog


fruits = ("사과", "배", "포도", "귤", "딸기")

a, *rest = fruits
print(a) 
print(rest)


x, y, *others = fruits
print(x, y) 
print(others)



