# -*- coding: utf-8 -*-

import math



#classe d'une action 
class act:
    def __init__(self,index,val,v1,v2) :
        self.index=index 
        self.val=val
        self.v1=v1
        self.v2=v2
         
    def display(self) :
        print(str(self.index)+" : " +str(self.val)+   " : ("+str(self.v1)+" ,"+str(self.v2) +")")

# classe de la pile
class jeu : 
    def __init__(self,init,tour):
        self.liste=init
        self.tour=tour
        
 # creer une copie identique du jeu    
    def copy(self) : 
        return jeu(self.liste.copy(),self.tour)
    
 # afficher la liste des piles     
    def display(self):
        print("la liste des piles = [" , end="")
        for x in self.liste :
            print(str(x)+',',end ="")
        print("]")
 # verifier si le jeu est terminé ou non    
    def isFinished(self):
        for x in self.liste :
            if (x>2):                
                return False        
        # if(self.tour==0):
        #    print(" MAX a perdu ")  ; 
        #else :
        #   print(" MIN a perdu " ) ; 
        return True
 # donner les atcions de deivision possible pour une liste des piles
    def actions(self) : 
        acts=[]
        for x in range(0,len(self.liste)) :
            if(self.liste[x]>2) : 
                for y in splitcases(self.liste[x]) :
                    acts.append(act(x,self.liste[x],y[0],y[1]))
        return acts    
 # deviser une pile dans un index donné  
    def split(self,index):
        if self.isFinished() :
            return False 
        elif (self.liste[index]>2) :
            x=0 ; 
            y=0 ;             
            while((x<=0)or(y<=0) or ((x+y)!= self.liste[index])) :                
                print("donner pile 1 : " , end="")
                x= int(input())
                print("donner pile 2 :" , end="")
                y= int(input())            
            self.liste[index]=x
            self.liste.insert(index+1,y)
            self.tour=(self.tour+1)%2 ; 
        else : 
            print("cette pile ne peut plus etre devisée ")        
# deviser  une pile dans un index en une pile de x et une pile de y             
    def directsplit(self,index,x,y):
        if self.isFinished() :
            return False 
        elif (self.liste[index]>2) :
            self.liste[index]=x
            self.liste.insert(index+1,y)
            self.tour=(self.tour+1)%2 ; 
        else : 
            print("cette pile ne peut plus etre devisée ")
            
# retourne les devisions possibles d'une seule pile 
def splitcases(x) : 
    result=[]
    for y in range(1,(x//2+x%2)) :
        result.append([y ,x-y] )
    return result 

# retourne  le score courant de jeu 
def utility(a) : 
    if(a.isFinished()) : 
        if a.tour == 0 :
            return -1 
        else : 
            return 1 

 
# deviser  une pile dans un index en une pile de x et une pile de y             
def result(j,index,x,y):
    b=j.copy()
    if b.isFinished() :
        return False 
    elif (b.liste[index]>2) :
        b.liste[index]=x
        b.liste.insert(index+1,y)
        b.tour=(b.tour+1)%2 ; 
        return b 
    else : 
        print("cette pile ne peut plus etre devisée ")
        return None  
    
#algorithme minimax    
def minimax(s) :
    
    
    results ={}
    if(s.isFinished()):
        print("A")
        return (utility(s),[],[])
    else  :
        actions = s.actions()
        children=[]
        for y in actions : 
            noeud=result(s,y.index,y.v1,y.v2)
            children.append(noeud)
            (mm,ll,ff) = minimax(noeud)
            children = children+ff
            results[str(mm)]=(y,ll+[y])

        
        
        # for y in results : 
        #    somme=somme+results[y][1]
        
        if (s.tour == 0 ):
           # print("C  Max joue"
            if("1" in results):
                print("max joue " , end="" ) 
                print(results["1"][0].display())
                #moves.append(results["1"])
                #print(results)
                return (1,results["1"][1],children)
            else:
                print("max joue" , end="" ) 
                print(results["-1"][0].display())
                #moves.append(results["-1"])
               # print(results)
                return (-1,results["-1"][1],children)
            
        else : 
            
            if("-1" in results):
                print("min joue" , end="" ) 
                print(results["-1"][0].display())
                #moves.append(results["-1"])
                #print(results)
                return (-1,results["-1"][1],children)
            else:
                print("min joue" , end="" ) 
                print(results["1"][0].display())
                #moves.append(results["1"])
                #print(results)
                return (1,results["1"][1],children)

# Max_value 
def max_value(s) : 
    if(s.isFinished()) :
        return utility(s) 
    else :
        actions = s.actions()
        maxv= float("-inf")
        for y in actions : 
            maxv =  max([maxv,min_value(result(s,y.index,y.v1,y.v2))])
        return maxv 

#Min_value 
def min_value(s) : 
    if(s.isFinished()) :
        return utility(s)
    else : 
        actions = s.actions()
        minv= float("inf")
        for y in actions : 
            minv= min([minv,max_value(result(s,y.index,y.v1,y.v2))])
        return minv

#MINIMAX_decision 
def minimax_decision(s) : 
    actions= s.actions()
    maxv=float("-inf")
    for y in actions : 
        m = min_value(result(s,y.index,y.v1,y.v2))
        if(m>maxv):
            maxv=m 
            maxact=y
    return maxact
          
# jouer le jeu avec deux jouers         
def twopersplay() :
    print("donner le nombre initial des jetons de la pile : " , end="")        
    n=int(input())
    j=-1 ; 
    while((j!=0)and ((j!=1))) :
        print("donner le joueur qui va commencer ")
        print("0 : MAX")
        print("1 : MIN ")
        j=int(input())
    a = jeu([n],j)
    while (not a.isFinished()) :
        if(a.tour==0):
            print("c'est le tour de MAX ")  ; 
        else :
            print("c'est le tour de MIN" ) ; 
        a.display()
        print("donner l'index de pile à deviser " , end='')
        h=int(input())
        while h>=len(a.liste) :
            h=int(input())
        a.split(h)
        a.display()

# Les 2 joueurs seront la machine et un utilisateur du programme.
def one_o_one() :
    print("donner le nombre initial des jetons de la pile : " , end="")        
    n=int(input())
    j=-1 ; 
    while((j!=0)and ((j!=1))) :
        print("donner le joueur qui va commencer ")
        print("0 : MAX")
        print("1 : MIN ")
        j=int(input())
    a = jeu([n],j)
    while (not a.isFinished()) :
        if(a.tour==1):
            print("c'est le tour de MIN" )  
            a.display()
            print("donner l'index de pile à deviser " , end='')
            h=int(input())
            while h>=len(a.liste) :
                h=int(input())
            a.split(h)
        else :
            print("c'est le tour de Max ") 
            d=minimax_decision(a)    
            d.display()
            a.directsplit(d.index, d.v1, d.v2)
    result=a.isFinished() 
    if(result):
        if(a.tour == 1 ):
            print("max gagne")
        else : 
            print("min gagne")
            
def one_o_one_alpha_beta() :
    print("donner le nombre initial des jetons de la pile : " , end="")        
    n=int(input())
    j=-1 ; 
    while((j!=0)and ((j!=1))) :
        print("donner le joueur qui va commencer ")
        print("0 : MAX")
        print("1 : MIN ")
        j=int(input())
    a = jeu([n],j)
    while (not a.isFinished()) :
        if(a.tour==1):
            print("c'est le tour de MIN" )  
            a.display()
            print("donner l'index de pile à deviser " , end='')
            h=int(input())
            while h>=len(a.liste) :
                h=int(input())
            a.split(h)
        else :
            print("c'est le tour de Max ") 
            (d,v)=alphabeta_decision(a)
            print("//////////////////////////")
            print("tous les noeuds visités")
            print("noeuds visité ", len(v))
            for y in v : 
                y.display()
            d.display()
            a.directsplit(d.index, d.v1, d.v2)
    result=a.isFinished() 
    if(result):
        if(a.tour == 1 ):
            print("max gagne")
        else : 
            print("min gagne")
    
def alphabeta(s, a , b, v):
    v.append(s)
    if (s.isFinished()):
      return utility(s)
    Alpha = a
    Beta = b
    
    if (s.tour == 1):
        actions = s.actions()
        for y in actions : 
           Beta = min(Beta, alphabeta(result(s,y.index,y.v1,y.v2), Alpha, Beta,v))
           if (Alpha >= Beta):
               return Alpha
        return Beta
    else:
        actions = s.actions()
        for y in actions : 
           Alpha = max(Alpha, alphabeta(result(s,y.index,y.v1,y.v2), Alpha, Beta,v))
           if (Alpha >= Beta):
               return Beta
        return Alpha
    
def alphabeta_decision(s):
    v = [s]
    if(s.tour == 0):
     actions = s.actions()
     for y in actions :
            result(s,y.index,y.v1,y.v2).display()
            res = alphabeta(result(s,y.index,y.v1,y.v2), -math.inf, math.inf,v)
            if(res == 1):
                return (y,v)
     return (actions[0],v)
    else:
     actions = s.actions()
     for y in actions :
            res = alphabeta(result(s,y.index,y.v1,y.v2), -math.inf, math.inf,v)
            if(res == -1):
                return (y,v)
     return (actions[0],v)

    
# main 

print("************JEU MINIMAX****************\n")
print("1- Un vs Minimax\n")
print("2- Un vs AlphaBeta \n")
print("0- Sortir\n")

res = input()

if(res == "1"):
    one_o_one()
elif(res == "2"):
    one_o_one_alpha_beta()
    

        
#h = jeu([5],0) 

#resultat = alphabeta(h, -math.inf, math.inf)
#print(resultat)
#print(minimax_decision(h))
#one_o_one_alpha_beta()

#resultat=minimax(h)
#print("//////////////////////////")
#print("tous les noeuds visités")
#for y in resultat[2] : 
#    y.display()
    
#print("la sequence d'action' : " )
#resultat[1].reverse()
#for y in resultat[1] : 
#    y.display()

#if(resultat[0] == 1) : 
#    print("Max gagne ")
#else : 
#   print("Min gagne ")


        
        






