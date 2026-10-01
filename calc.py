num1=input("enter number 1 ")
num2=input("enter nuber 2  ")
num1=int(num1)
num2=int(num2)
#----------------------------------------------
print ("what will happen to this numbers?")
#-------------------------------------------
ent1=input("enter A for plus , " \
"enter B for minus" \
"enter C for zarb " \
"enter D for dividing  :")
#---------------------------------------------
def jam():
    jam=num1+num2 
    print("hasele jam" )
    print(jam)
#------------------
def menha():
    menha=num1-num2
    print("hasele menha")
    print(menha)
#------------------
def zarb():
    zarb=num1*num2
    print("hasele zarb")
    print(zarb) 
#------------------
def taqsim():
    taqsim=num1/num2
    print("hasele taqsim")
    print(taqsim)    
#---------------------------------------------
if ent1=="A":
   jam()
#------
if ent1=="B":
    menha()
#------
if ent1=="C":
    zarb()    
#------
if ent1=="B":
    taqsim()
#------------------------------    
        
