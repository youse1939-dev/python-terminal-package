print("welcome to shape calc")

print("what sahpe do you want to calculate ?")

CHOOSE=input("squar or circle?")
#-------------------------------------------------
def area_of_circle():
    r=float(input("enter the radius of the circle :"))
    area=3.14*r*r
    print("the area of the circle is :",area)
#---------------------------
def Circumference_of_circle():
    r=float(input("enter the radius of the circle :"))
    circumference=2*3.14*r
    print("the circumference of the circle is :",circumference)
#----------------------------------------------------
def area_of_square():
    s=float(input("enter the side of the square :"))
    area=s*s
    print("the area of the square is :",area)
#---------------------------
def Circumference_of_squre():
    s=float(input("enter the side of the square :"))
    Circumference=s*4
    print("the Circumference of the squar id :",Circumference)
#----------------------------------------------------------------


#--------------------------------------------------
if CHOOSE=="squar":
  choose2=input("area of squar or Circumference ? :")
  if choose2=="area":
      area_of_square()
  else:
      Circumference_of_squre()
#-----------------------------------
elif CHOOSE=="circle":
  choose2=input("area of circle or Circumference ? :")
  if choose2=="area":
      area_of_circle()  
  else:
      Circumference_of_circle()
else:
    print("invalid input")
#---------------------------------------------------

