import pygame
import time
import random

width,height=1200,600

black =(0,0,0)
red =(255,0,0)
green =(0,255,0)
blue =(0,0,255)
yellow=(255,255,0)
Magenta =(255,0,255)
cyan=(0,255,255)

pygame.display.init()

display=pygame.display.set_mode((width,height))
pygame.display.set_caption('BubbleSort')
list_A=[]
list_X=[]

for i in range(0,width,5):

    r=random.randint(0,height)
    pygame.draw.line(display,red,(i,600),(i,r),5)
    pygame.display.update()
    list_X.append(i)
    list_A.append(r)
time.sleep(2)

for i in range(len(list_A)-1):
    for c in range(len(list_A)-i-1):
    

        if (list_A[c])<(list_A[c+1]):

            list_A[c],list_A[c+1]=list_A[c+1],list_A[c]
            

    display.fill(black)
    
    for u in range (len(list_X)):
        pygame.draw.line(display,blue,(list_X[u],600),(list_X[u],list_A[u]),5)
    pygame.display.update()
    time.sleep(0.05)
    
time.sleep(5)

pygame.quit()
