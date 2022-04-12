# Author: John Thomas
# netID: jat710
#
# Description: A short program designed to calculate the 

import pytest


from cProfile import run
from unittest import result



def bmiCalculator(feet,inches,lbs):
    metLbs = lbs*0.45
    metHeight = ((feet*12) + inches) * 0.025
    metHeightSquared = metHeight*metHeight
    return (metLbs / metHeightSquared)
    
def bmiResult(bmi):
    category = ""
    if(bmi < 18.5):
        category = "Underweight"
    elif(bmi >= 18.5 and bmi <= 24.9):
        category = "Normal"
    elif(bmi>=25 and bmi <= 29.9):
        category = "Overweight"
    else:
        category = "Obese"
    return category

def main():
    print("Please imput th1e variables to calculate your BMI. \nHeight")
    feet = float(input("Feet: "))
    inches = float(input("Inches: "))
    lbs = float(input("Weight:\nPounds: "))
    bmi = bmiCalculator(feet,inches,lbs)
    print(bmi)
    print("Your BMI result is: ", bmi)
    result = bmiResult(bmi)
    print("Your Category: ", result)
    
    input("PRESS ENTER TO CONTINUE")
   
    
    
    
if __name__ == "__main__":
    main()