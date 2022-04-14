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
    bird.setMotors(0,25)      #Makes Finch turn Left
    sleep(3.5)                #Pauses the execution of the Program for 3.5 Seconds
    bird.setMove('F',15,30)   #Moves the Finch Forward 15 Centimeters
    bird.setMotors(25,0)      #Makes Finch Turn Right
    bird.setMove('F',15,30)   #Moves the Finch 15 Centimeters
    sleep(4)                  #Pauses the execution of the Program for 4 Seconds 
    bird.stopAll()            #Completely stops the Program

def exercise4():
    color = input("Please enter a letter:")
    if (color == 'g'):
        bird.setBeak(0,100,0)

    else:
        print('Sorry, that is not my favorite letter!')
    sleep(1)
    bird.stopAll()

def exercise5():
    color = input("Please enter a letter:") #Allows the Program to ask the user a Question
    if (color == 'r'): #Tells the Program what letter the user wants
        bird.setTurn('R',70,50) #Turns the Finch to the Right

    else:
        print('To Bad so Sad you got it Wrong!')
        bird.setTurn('L',70,50)

def exercise6():        
    

    


#exercise1()
#exercise2()
#exercise3()
#exercise4()
#exercise5()
        


