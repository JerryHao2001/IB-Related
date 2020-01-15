limit = 4

value=[20,6,38,50,40]

for counter1 in range(0,limit):
    minimum = counter1
    for counter2 in range(counter1+1,limit+1):
        if value[counter2] < value[minimum]:
            minimum = counter2
    if minimum != counter1:
        value[minimum],value[counter1] = value[counter1],value[minimum]
print(value)