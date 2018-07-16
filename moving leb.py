x=50
xSpeed = 1
def setup():
    fullScreen()


def draw():
    background(0)
    global x, xSeed
    fill(random(255),0,0)
    rect(x,height/2,150,75)
    x= x+xSpeed
    
    # display xSpeed
    fill(255)
    text("xSpeed: " + str(xSpeed), width/2, 32)
    
def mouseClicked():
    global xSpeed 
    # xSpeed=xSpeed * -1
    
    print("x:",x)
    if (( mouseX > x and mouseX < x+150)):
        if ((mouseY > height/2) and (mouseY < height/2 +75)):
            xSpeed=xSpeed *-1
            if (xSpeed >= 0):
                xSpeed +=1
            else:
                xSpeed += -1
            
    #     print("it works!")
    # print(mouseX, mouseY)   
    # if (xSpeed==1):
    #     xSpeed=-1
    # elif (xSpeed ==-1):
    #     xSpeed=1
