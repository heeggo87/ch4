cart = { '사과':3, '바나나':5, '딸기':2 }
print(cart) #{'사과': 3, '바나나': 5, '딸기': 2}


cart['사과'] = 10
print(cart) #{'사과': 10, '바나나': 5, '딸기': 2}

del cart['바나나']
print(cart) #{'사과': 10, '딸기': 2}

print('')



score = { '수학':95 }

score['영어'] = 88
score['국어'] = 100

print(score)


cafe_menu = { '아메리카노':2000, '라떼':3000, '케이크':4500 }

cafe_menu['아메리카노'] = 2500

del cafe_menu['케이크']

print(cafe_menu)
