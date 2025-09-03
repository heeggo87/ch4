fruits =[]
fruits.append('사과')
fruits.append('바나나')
fruits.append('포도')
print(fruits) #['사과', '바나나', '포도']


numbers = [10, 20, 30, 40]
numbers[1] = 99
print(numbers) #[10, 99, 30, 40]


animals = ['강아지', '고양이', '토끼']
animals.remove('강아지')
print(animals) #['고양이', '토끼']


subjects = ["국어", "영어", "수학", "과학"]
del subjects[1]
print(subjects) #['국어', '수학', '과학']


scores = [70, 80, 90, 100]
last = scores.pop()
print(scores, last) #[70, 80, 90] 100