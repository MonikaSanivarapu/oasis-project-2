weight = float(input("Please Enter your weight in kg: "))
height = float(input("Please Enter your height in centimeters: "))

height_in_meters = height / 100
BMI = weight / (height_in_meters**2)
print(BMI)

if (BMI < 16):
    print ("Present You are severely underweight"), BMI

elif (BMI >= 16 and BMI < 18.5):   
    print ("Present You are Underweight"), BMI

elif (BMI >= 18.5 and BMI < 24):
    print ("Present You are Healthy"), BMI

elif (BMI >= 25 and BMI < 30):
   print ("Present You are Overweight"), BMI

elif (BMI >=30):
    print ("Present You are Obese"), BMI