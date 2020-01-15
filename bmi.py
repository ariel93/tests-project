
def BMInum(weight, height):
    '''
    This function will calculate the BMI - Body Mass Index.
    it is a value derived from the mass (weight) and height of a person.
    :param weight: The weight of a person in kg
    :param height: The height of a person in m and cm
    :return: the unit BMI that represent the weight divided by height pow by 2
    '''
    try:
        return weight / height ** 2
    except ZeroDivisionError:
        print("ZeroDivisionError")

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
