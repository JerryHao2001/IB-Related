import turtle 
t = turtle.Turtle()
t.speed(50)
t.penup()

def H(time,l,x=0,y=0):
    t.goto(x-l/2,y+l)
    t.pendown()
    t.goto(x-l/2,y-l)
    t.goto(x-l/2,y)
    t.goto(x+l/2,y)
    t.goto(x+l/2,y+l)
    t.goto(x+l/2,y-l)
    t.penup()
    ed1,ed2,ed3,ed4 = (x+l/2,y+l),(x+l/2,y-l),(x-l/2,y+l),(x-l/2,y-l)
    if time>1:
        H(time-1,l/2,ed1[0],ed1[1])
        H(time-1,l/2,ed2[0],ed2[1])
        H(time-1,l/2,ed3[0],ed3[1])
        H(time-1,l/2,ed4[0],ed4[1])

if __name__ == "__main__":
    H(5,100)
    