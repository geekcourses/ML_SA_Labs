w = float( input('Enter weight in kg:') )
h = float( input('Enter height in cm:') )
hm = h/100

bmi = w / hm**2
bmi =round(bmi, 2)

print(f'BMI={bmi}')