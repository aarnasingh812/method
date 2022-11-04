#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      aarna
#
# Created:     04/11/2022
# Copyright:   (c) aarna 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Method Overloading
import math

def volume(arg1, arg2 = None, arg3 = None):
    if(arg1==arg2==arg3):
        print("volume of cube :",arg1**3)

    elif(arg3==None and arg2!=None):
        print("volume of cylinder :",(arg1**2)*arg2*3.14)

    elif(arg2==None and arg3==None):
        print("volume of sphere :",(4/3)*3.14*(arg1**3))

    else:
        print("volume of cuboid :",arg1*arg2*arg3)

#Method call

volume(2.2,3.5,5)
volume(6,10)
volume(4.5)
volume(6,6,6)
