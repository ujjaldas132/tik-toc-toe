from turtle import *
speed(10)
def circle_draw(x_center,y_center,radius):
                up()
                goto(x_center,y_center-radius)
                down()
                color('black')
                circle(radius)


def cross_draw(x_center,y_center,half_side_length):
                color('red')
                for i in range(4):
                                left(45)
                                up()
                                goto(x_center,y_center)
                                down()
                                forward(half_side_length)
                                left(45)



#setting th epensize
def box():

                up()
                goto(50,150)
                down()
                sety(-300)
                up()
                goto(-50,150)
                down()
                sety(-300)
                up()
                goto(-150,50)
                down()
                setx(300)
                up()
                goto(-150,-50)
                down()
                setx(300)



def draw(i,centers,j):
                if j%2==0:
                                circle_draw(centers[i][0],centers[i][1],20)
                else:
                                cross_draw(centers[i][0],centers[i][1],20)



                




