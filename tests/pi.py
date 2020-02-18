import random

def calculate_pi(n):
    count = 0
    for i in range(n):
        a,b = random.random(),random.random()
        if (((a-0.5)**2 + (b-0.5)**2)**0.5) <= 0.5:
            count += 1
    print(count/n*4)

calculate_pi(40000000)


