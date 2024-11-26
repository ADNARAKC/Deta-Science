height=int(input("Enter your height in meters: "))
weight=int(input("Enter your weight in kg: "))
bmi = weight/height**2
if bmi<18.5:
    print("Under weight")
elif bmi>18.5 and bmi<24.9:
    ptint("Normal Weight")
elif bmi>24.9 and bmi<29.9:
    print("Over weight")
elif bmi>29.9 and bmi<30:
    print("Obese")
else:
    print("You are severely obese")