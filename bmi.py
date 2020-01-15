# the function get weight (kg) and height(m) and return the BMI number
def BMInum(weight, height):
    if height == 0.0:
        return 'ZeroDivisionError'
    else:
        return weight / height ** 2


# the function return the BMI solution by the BMI  number
def BMIsolution(BMI_number):
    BMIdictionary = {
        15: 'Very severely underweight',
        16: 'severely underweight',
        18.5: 'Underweight',
        25: 'Normal (healthy weight)',
        30: 'Overweight',
        35: 'Obese Class I (Moderately obese)',
        40: 'Obese Class II (Severely obese)',
        45: 'Obese Class III (Very severely obese)',
        50: 'Obese Class IV (Morbidly obese)',
        60: 'Obese Class V (Super obese)',
        61: 'Obese Class VI (Hyper obese)'
    }
    for status in BMIdictionary:
        if BMI_number < status:
            return BMIdictionary[status]
    return BMIdictionary[61]
