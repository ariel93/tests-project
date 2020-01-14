

# the function get weight (kg) and height(m) and return the BMI number
def BMInum(weight,height):
    if height == 0.0:
        return 'ZeroDivisionError'
    else:
        return weight/height**2


# the function return the BMI solution by the BMI  number
def BMIsolution(BMI_number):
    if BMI_number<15 :
        return "Very severely underweight"
    if BMI_number>=15 & BMI_number<16 :
        return "severely underweight"
    if BMI_number>=16 & BMI_number<18.5 :
        return "Underweight"
    if BMI_number>=18.5 & BMI_number<25 :
        return "Normal (healthy weight)"
    if BMI_number>=25 & BMI_number<30 :
        return "Overweight"
    if BMI_number>=30 & BMI_number<35 :
        return "Obese Class I (Moderately obese)"
    if BMI_number>=35 & BMI_number<40 :
        return "Obese Class II (Severely obese)"
    if BMI_number>=40 & BMI_number<45 :
        return "Obese Class III (Very severely obese)"
    if BMI_number>=45 & BMI_number<50 :
        return "Obese Class IV (Morbidly obese)"                  				
    if BMI_number>=50 & BMI_number<60 :
        return "Obese Class V (Super obese)"  
    if BMI_number>=60 :
        return "Obese Class VI (Hyper obese)"      
	