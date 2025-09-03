# 객체 비교하기 (is ==)

# 리스트 생성
a = [1,2,3]

# a 를 복사
b = a
c = [1,2,3]

# is : 두 변수가 같은 객체를 가리키는지
print(a is b) #true
print(a is c) #false

# == : 두 변수가 같은 내용을 가지고 있는지
print(a == b) #true
print(a == c) #true

print(a is not b) #false
