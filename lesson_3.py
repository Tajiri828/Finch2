from BirdBrain import Finch
from time import sleep
bird = Finch("A")
def exercise2():
    bird.setBeak(100,0,100)
    bird.setBeak(0,0,50)
    bird.setTail(1,0,100,0)
    sleep(5)
    bird.setTail(2,100,0,100)
    sleep(5)
    bird.setTail("all",0,100,0)
    sleep(5)
    bird.stopAll()
    

def exercise3():
    bird.setTail(1,0,100,0)
  

def exercise4():
    bird.setBeak(100,0,0)
    bird.setTail(1,100,64,0)
    bird.setTail(2,100,100,0)
    bird.setTail(3,0,0,100)
    bird.setTail(4,100,0,100)
    sleep(2)
    bird.stopAll()

def exercise5():
    userResponse = input("Which tail light (1-4) should be red? ")
    number = int(userResponse)
    bird.setTail(number,100,0,0)
    sleep(1)
    bird.stopAll()

def exercise6():
    redIntensity = int(input("Choose a Value for Red"))
    greenIntensity = int(input("Choose a value for Green"))
    blueIntensity = int(input("Choose a value for Blue"))
    bird.setBeak(redIntensity,greenIntensity,blueIntensity)
    bird.setTail("all",redIntensity,greenIntensity,blueIntensity)

def exercise7():
    bird.setTail(1,100,0,0)
    bird.setMove('F',25,50)
    bird.setTurn('R',90,50)
    bird.setMove('F',25,50)
    bird.setTail(2,100,64,0)
    bird.setTurn('R',90,50)
    bird.setMove('F',25,50)
    bird.setTail(3,100,100,0)
    bird.setTurn('R',90,50)
    bird.setMove('F',25,50)
    bird.setTail(4,100,0,100)
    bird.setTurn('R',90,50)
    bird.setMove('F',25,50)
    sleep(1)
    bird.stopAll()
   
    


    
    

                       

#exercise2()
#exercise3()
#exercise4()
#exercise5()
#exercise6()
#exercise7()
