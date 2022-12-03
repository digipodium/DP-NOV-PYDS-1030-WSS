ques = "What is an Elephant"
oA = "An Insect"
oB = "A Mammal"
oC = "A Bird"
oD = "A Reptile"
correct = 'B' 
print("Welcome to the quiz")
print(ques)
print('-' * 20)
print(f'A. {oA}') # f-string
print(f'b) {oB}')
print(f'c) {oC}')
print(f'd) {oD}')
print('-' * 20)

ans = input('Enter your answer: ')
if ans.upper() == correct:
    print('Correct ✅')
else:
    print('Incorrect ❌🤔')