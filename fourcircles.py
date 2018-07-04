t2, t3, t4 = 0, 0, 0
def setup():
    size(600, 600)
    background(0)
                
def draw():
    global t2, t3, t4
    background(0)
    # first circle
    ellipse(height*1/5,random(width), 10, 10)
    
    # second cirle
    x2 = noise(t2)
    x2 = map(x2, 0, 1, 0, width)
    ellipse( height*2/5,x2, 20, 20)
    t2 += 1
    
    # third cirle
    x3 = noise(t3)
    x3 = map(x3, 0, 1, 0, width)
    ellipse( height*3/5,x3, 30, 30)
    t3 += .05
    
    # fourth cirle
    x4 = noise(t4)
    x4 = map(x4, 0, 1, 0, width)
    ellipse( height*4/5,x4, 70, 70)
    t4 += .01
