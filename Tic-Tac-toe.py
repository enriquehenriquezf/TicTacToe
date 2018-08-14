# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:52:18 2018

@author: jjose
"""




import numpy as np
import random



Mapa=np.array([[0,0,0],[0,0,0],[0,0,0]])
Fila=random.randint(0, 2)
Columna=random.randint(0, 2)
Mapa[Fila][Columna]=1
print(Mapa)


def Jugado1(Mapa):
    A=0
    for i in range(3):
     for j in range(3):
         if Mapa[i][j] == 0:
             A=A+1         
    print (A)
    
#def ganar (Mapa):
  #  if(Mapa[0][0] == 1):
 #       J1=1


Jugado1(Mapa)


def check_status():       
# any vertical combination
    for i in range(0,9,3):
        if Mapa[i//3][0]!=0 and Mapa[i//3][0]==Mapa[i//3][1]==Mapa[i//3][2]:
            return Mapa[i//3][0]
    
    # any horizontal combination    
    for i in range(3):
        if Mapa[0][i]!=0 and Mapa[0][i]==Mapa[1][i]==Mapa[2][i]:
            return Mapa[0][i]    
    
    #for diagonal combination
    if Mapa[0][0]!=0 and Mapa[0][0]==Mapa[1][1]==Mapa[2][2]:
        return Mapa[0][0]
    if Mapa[0][2]!=0 and Mapa[0][2]==Mapa[1][1]==Mapa[2][0]:
        return Mapa[0][2]
    
    #if more moves possible
    for i in range(0,2):
        for j in range(0,2):
            if Mapa[i][j] ==0:
                return -1
    
    #if no winner---tie
    return 0


   
#minimax algorithm with apha beta cuts
def minimax(isMax,alpha,beta):
    status=check_status()
    if status==1:
        return 10
    elif status==2:
        return -10
    elif status==0:
        return 0

    if(isMax):
        best=-1000000
        for i in range(0,2):
            for j in range(0,2):
                
                if Mapa[i][j]==0:
                    Mapa[i][j]=1
                    val=minimax(not isMax,alpha,beta)
                    Mapa[i][j]=0
                    best=max(best,val)
                    alpha=max(alpha,best)
    
                    if beta<=alpha:
                        return alpha

        return alpha

    else:
        best=1000000
        for i in range(0,2):
            for j in range(0,2):
                if Mapa[i][j]==0:
                    Mapa[i][j]=2
                    val=minimax(not isMax,alpha,beta)
                    Mapa[i][j]=0
                    best=min(best,val)
                    beta=min(beta,best)
    
                    if beta<=alpha:
                        return beta

        return beta



def alphabeta(sw):
    bestval=-1000000
    pos =-1
    for i in range(3):
            for j in range(3):
                if Mapa[i][j]==0:
                    Mapa[i][j]=1
                    moveval=minimax(sw,-1000000,1000000)
                    Mapa[i][j]=0
                    if moveval > bestval:
                        bestval=moveval
                        pos = i*3 + j
    return pos    
                            
        					
        				#print arr
k = 1   
sw = False             			 
while k < 9 :                                                     				
    iaID = alphabeta(sw)
    Fila = iaID // 3
    Columna = iaID - (3*Fila)
    if k % 2 == 1:
        Mapa[Fila][Columna] = 2
        sw = True
    else:
        Mapa[Fila][Columna] = 1
        sw = False
    print(Mapa)
    k = k+1