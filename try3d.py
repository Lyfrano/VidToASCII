import time
import os
import random
import keyboard

x,y,z =0,0,3
currentCluster = 0
i = 0
j = 0
ZMAX = 5
zSIZE = [".","*","o","O","@"]
CANVAS_SIZE = [30,40]

def randomMoveObject():
    direction = random.randint(1,3)
    value = random.randint(-1,1)
    return direction,value

class dot:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def isMoveLegal(self, value, direction):
        if direction == 1:
            if self.x + value < 0 or self.x + value >= CANVAS_SIZE[1]:
                return False
        if direction == 2:
            if self.y + value < 0 or self.y + value >= CANVAS_SIZE[0]:
                return False
        if direction == 3:
            if self.z + value < 0 or self.z + value >= ZMAX:
                return False
        return True

class cluster:
    def __init__(self):
        self.dots = []
    def addDot(self,dot):
        self.dots.append(dot)
    def move(self,value,direction):
        temp = self.dots.copy()


        if self.isMoveLegal(value,direction) == False:
            return False
        for dot in self.dots:
                if direction == 1 :
                    dot.x += value
                if direction == 2 :
                    dot.y += value
                if direction == 3 :
                    dot.z += value


    def makeCube(self):
        self.dots = []
        self.dots.append(dot(0,3,4))
        self.dots.append(dot(1,3,4))
        self.dots.append(dot(2,3,4))
        self.dots.append(dot(3,3,4))

        self.dots.append(dot(1,4,4))
        self.dots.append(dot(2,4,4))

        self.dots.append(dot(1,5,4))
        self.dots.append(dot(2,5,4))

        self.dots.append(dot(0,4,4))
        self.dots.append(dot(0,5,4))
        self.dots.append(dot(0,6,4))

        self.dots.append(dot(1,6,4))
        self.dots.append(dot(2,6,4))
        self.dots.append(dot(3,6,4))

        self.dots.append(dot(3,4,4))
        self.dots.append(dot(3,5,4))
        self.dots.append(dot(3,6,4))

        self.dots.append(dot(1,2,3))
        self.dots.append(dot(4,2,3))
        self.dots.append(dot(4,5,3))

        self.dots.append(dot(2,1,2))
        self.dots.append(dot(3,1,2))
        self.dots.append(dot(4,1,2))
        self.dots.append(dot(5,1,2))
        self.dots.append(dot(5,4,2))
        self.dots.append(dot(5,3,2))
        self.dots.append(dot(5,2,2))
        self.dots.append(dot(5,2,2))


    def isMoveLegal(self,value,direction):
        for dot in self.dots:
            if direction == 1 :
                if dot.x + value < 0 or dot.x + value == CANVAS_SIZE[1]:
                    return False
            if direction == 2 :
                if dot.y + value < 0 or dot.y + value == CANVAS_SIZE[0]:
                    return False
            if direction == 3 :
                if dot.z + value < 0 or dot.z + value >= ZMAX:
                    return False
        return True
            
                

clusters = []
def getKeyPress():
    
    global currentCluster


    if keyboard.is_pressed('w'):
        return 2, -1
    if keyboard.is_pressed('s'):
        return 2, 1
    if keyboard.is_pressed('a'):
        return 1, -1
    if keyboard.is_pressed('d'):
        return 1, 1
    if keyboard.is_pressed('q'):
        return 3, -1
    if keyboard.is_pressed('e'):
        return 3, 1
    if keyboard.is_pressed('space'):
        clusters.append(cluster())

        currentCluster += 1

        clusters[currentCluster].makeCube()

    return None, None

def getTopPixelAt(x,y):
    global z
    z = -1
    for cluster in clusters:
        for d in cluster.dots:
            if d.x == x and d.y == y:
                if d.z > z:
                    z = d.z
    return z


def main():
    cluster1 = cluster()
    cluster1.makeCube()
    clusters.append(cluster1)
    

    while True :
        drawCanvas()
        
        keyboard.read_event()

        direction, value = getKeyPress()
        clusters[currentCluster].move(value, direction)

        
        




def drawBlankCanvas():
    for i in range(CANVAS_SIZE[0]):
        print('')
        for j in range(CANVAS_SIZE[1]):
            print(" . ", end='')

def drawCanvas():

    global z

    z = 0

    os.system('cls' if os.name == 'nt' else 'clear')

    print('')
    for i in range(CANVAS_SIZE[1]):
        print('---',end = '')
        

    for i in range(CANVAS_SIZE[0]):
        print('|')
        for j in range(CANVAS_SIZE[1]):
            z = getTopPixelAt(j,i)
            if z == -1:
                print("   ", end='')
            else:
                print(" "+ zSIZE[z] + " ", end='')

    print('')


if __name__ == "__main__":
    main()