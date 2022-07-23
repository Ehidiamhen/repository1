Height = float(input("Enter you Height in centimetres: "))
Weight = float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI = Weight/(Height*Height)
print("Your Body Mass Index is: ",BMI)
if (BMI>0):
    if (BMI<=16):
        print("You are Severly Underweight")
    elif(BMI<=18.5):
        print("You are Underweight")
    elif(BMI<=25):
        print("You are Healthy!")
    elif(BMI<=30):
        print("You are Overweight")
    else:
        print("You are Severely Overweight")
else:
    ("Enter Valid Details")