def main():
    weight = float(input("Enter weight (in kg): "))
    height = float(input("Enter height (in cm): "))
    bmi = weight / ((height / 100)**2)
    bmi = 40
    print(bmi)
    if bmi < 18.5 :
        print("Underweight")
    elif bmi >= 18.5 and bmi < 25.0 :
        print("Normal weight")
    elif bmi >= 25.0 and bmi < 30.0 :
        print("Increased weight")
    elif bmi >= 30 and bmi < 40 :
        print("Obese")
    elif bmi >= 40 :
        print("Very high obese")

main()
    