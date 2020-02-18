import random
score = 0
def play():
    global score
    operater = random.choice(['+','-','*','/'])
    X,Y = str(random.randint(0,100)),str(random.randint(0,100))
    answer = eval(X+operater+Y)
    print(X,operater,Y)
    user_answer = eval(input("input ur answer!"))

    if answer == user_answer:
        print('correct')
        score += 1
    else:
        print('incorrect, correct answer is {}'.format(answer))

play()