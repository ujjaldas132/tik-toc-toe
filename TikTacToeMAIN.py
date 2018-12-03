from results_check import check
from matrixPrint import display
import numpy as np
from visual import *
from turtle import *

class attempt:
                def __init__(self):
                                self.count=1
attempt=attempt()


#increase the speed of the pen
speed(10)
#####

screen=Screen()
screen.title("BOXES")
centers=[[-100,100],[0,100],[100,100],[-100,0],[0,0],[100,0],[-100,-100],[0,-100],[100,-100]]
width=300
height=300
startx=0
starty=0
screen.setup(width,height,startx,starty)
"""*****"""
#pen size
pensize(5)
#draw the box
box()




##screen clicking
def clicked(x,y):
                if attempt.count<10:
                                print(x,y)
                                x=abs(x+150)
                                y=abs(y-150)
                                row=int(x/100)
                                col=int(y/100)
                                #print("cordinate>>",row,">",col)
                                square_no=(row+1+(col*3))
                                taking_input(square_no)
                                #print("sqaure no",square_no)
                                draw(square_no-1,centers,attempt.count)
                else:
                                print("\n\n")
                                print("\t\tMATCH IS OVER")
                                bye()
onscreenclick(clicked)




#size of the matrix of tic tok toe
n=3
#the matrix
matrix=np.zeros((n,n))


#dictionary to store some useful moves that can lead to win
data_dict={'user1':[],'user2':[]}
#user 1 put 1 and user2 put 2 in the matrix
#print("me")

"""
how to fill the matrix
"""
coordinates=[]
for i in range(n):
                for j in range(n):
                                coordinates=coordinates+[[i,j]]

def taking_input(square_no):
                [x,y]=coordinates[square_no-1]
                #print("X Y",x,y)

                user=""

                if attempt.count%2==0:
                                user='user2'
                                matrix[x][y]=2
                else:
                                user='user1'
                                matrix[x][y]=1

                attempt.count+=1
                if x==0 or y==0:
                                data_dict[user]=data_dict[user]+[[x,y]]

                if(check(matrix,n,user,data_dict)==1):
                                print("\n\n")
                                print("***\t****\t****",user+" win")
                                print("\n\n")
                                print("CLICK TO CLOSE THE WINDOW AND THEN RESTART")
                                attempt.count=10

                                                
