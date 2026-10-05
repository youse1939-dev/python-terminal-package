AVG=0
#----------------------------------------
e1=float(input("enter course 1 :"))

e2=float(input("enter course 2 :"))

e3=float(input("enter course 3 :"))

e4=float(input("enter course 4 :"))

AVG=(e1+e2+e3+e4)/4
#_-------------------------------------
def good():
   print("your avg is",AVG,)
   print("you got good ")
#------------------------------   
def exelent():
    print("your avg is",AVG,)
    print("you got Exelent ")
#_-----------------------------    
def bad ():
   print("your avg is",AVG,)
   print("you got messed up ")
#---------------------------------------

if AVG<10:
   bad()

elif AVG>18:
   exelent()

else:
   good()
