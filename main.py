def bmi_calculate(height, weight):
    bmi = weight / (height ** 2)
    if bmi >= 30:
        return 'Obese'
    elif bmi >= 25:
        return 'Overweight'
    elif bmi >= 18.5:
        return 'Normal'
    else:
        return 'Underweight'
bmi_calculate(1.8, 70)