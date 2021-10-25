from turtle import *
from random import randint
speed(-1)

def carre(l):
    for i in range(4):
        forward(l)
        left(90)
        
def carre_10(l):       
    for i in range(10):
        carre(l)
        penup()
        forward(l+5)
        pendown()

def carre_100():
    penup() , goto(-250,-250),pendown()
    for ii in range(1,11):
        carre_10(50)
        penup() , goto(-250,-250+ii*55),pendown()
def carre_commun():
    penup() , goto(-250,-250),pendown()
    l = 10
    for i in range(50):
        carre(l)
        l += 10
def carre_tournant(n):
    for i in range(n):
        carre(100)
        left(360/n)
carre_tournant(100)
#Q1 -360/n
#Q2
def polygone_reg_convexe(n,l):
    for i in range(n):
        forward(l)
        left(360/n)
#Q3
#polygone_reg_convexe(4,50)
#polygone_reg_convexe(5,50)
#polygone_reg_convexe(6,50)
#polygone_reg_convexe(7,50)
def polygone_reg_nonconvexe(n,l,k):
    right(180/n)
    for i in range(0,n):
        right(360/n*k)
        forward(l)
#polygone_reg_nonconvexe(10,100,3)
        
def tortue_sortie(x,y):
    if (x,y) >(-200,200) and (x,y) <(200,-200):
        return False
    else :
        return True

print(tortue_sortie(210,124))
print(tortue_sortie(150,130))
print(tortue_sortie(200,-200))
print(tortue_sortie(-220,120))
def mvt():
    penup() , goto(-200,-200),pendown()
    width(10)
    carre(400)
    width(1)
    penup() ,home(),pendown()
    while not tortue_sortie(xcor(), ycor()):
        color('green')
        forward(randint(10,30))
        left(randint(0,359))
        

def billard(width_B,height_B,x,y,angle_i,nb_bande):
    #draw_Billard
    penup() , goto(width_B/-2,height_B/-2),pendown(),width(7),color('brown')
    forward(width_B),left(90),forward(height_B),left(90),forward(width_B),left(90),forward(height_B),left(90)
    #FILL COLOR
    
#billard(400,200,0,0,90,5)
    