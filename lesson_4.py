from BirdBrain import Finch
from time import sleep
bird = Finch("A")
def exercise1():
    bird.setMotors(50,50)
    sleep(1)
    bird.stop()
    
def exercise2():
    userResponse = int(input("What is the speed of the right wheels? "))
    right = int(userResponse)
    userResponse = int(input("What is the speed of the left wheel? "))
    left = int(userResponse)
    bird.setMotors(left,right)
    sleep(2)
    bird.stopAll()

def exercise3():
    bird.setMotors(0,50)
    bird.setMotors(50,0)
    sleep(2)
    bird.stopAll()


    
#exercise1()
#exercise2()
exercise3()
