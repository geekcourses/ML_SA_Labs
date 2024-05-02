def get_user_data():
    """Retrieves user data from the command line
    	Arguments: none
    	Returns:
    		dictionary of the form:
    			{
    				"name" : "user_name",
    				"height": "user heigth in meters",
    				"weight": "user weight in kilograms"
    			}
    """

    bmi_dict = {}
    bmi_dict['name'] = input('Enter your name, please: ')
    while len(bmi_dict['name']) < 2 :                                                      # Task 2
        bmi_dict['name'] = input('Enter your name, please: ')

    # bmi_dict['height'] = float(input('I need to know your height in meters: '))
    # while bmi_dict['height'] < .50 or bmi_dict['height'] > 2.50:                           # Task 2
    #     bmi_dict['height'] = float(input('I need to know your height in meters: '))

    while True:
        bmi_dict['height'] = float(input('I need to know your height in meters: '))
        if .50<bmi_dict['height']<=2.50:
            break

    bmi_dict['weight'] = float(input('And your weight in kilograms: '))
    while bmi_dict['weight'] < 5 or bmi_dict['weight'] > 300:                              # Task 2
        bmi_dict['weight'] = float(input('And your weight in kilograms: '))
    return bmi_dict


def calc_BMI(w,h):
	"""Calculates the BMI, using formula bmi== w / (h*h)

		Arguments:
			w [float]: weight in kilograms
			h [float]: heigth in meters

		Returns:
			[float]: calculated BMI
	"""
	bmi = w / (h*h)
	return bmi


def calc_BMI_category(bmi):
    """Calculates the BMI category

        Arguments:
            bmi [float]: the bmi number index

        Returns:
            [string]: bmi category
    """
    if bmi < 16.0:
        return "Underweight (Severe thinness)"
    elif 16.0 <= bmi <=16.9:
        return "Underweight (Moderate thinness)"
    elif  17.0 <= bmi <=18.4:
        return "Underweight (Mild thinness)"
    elif  18.5 <= bmi <=24.9:
        return "Normal range"
    elif  25.0 <= bmi <=29.9:
        return "Overweight (Pre-obese)"
    elif  30.0 <= bmi <=34.9:
        return "Obese (Class I)"
    elif  35.0 <= bmi <=39.9:
        return "Obese (Class II)"
    elif bmi >= 40.0:
        return "Obese (Class II)"

def print_results(name,bmi,bmi_category):
    """Prints the BMI category
    	Arguments:
    		bmi_category [string]: bmi category
    """
    print('\n')
    print('*'*50)
    print(f'{name}, your BMI is {bmi:.2f}.  Category:  {bmi_category}')
    print('*'*50)


### TEST:
# get user data
user_data = get_user_data()

# # calculate BMI
bmi = calc_BMI(user_data["weight"],user_data["height"] )
print(bmi)
# # calculate BMI category
bmi_category = calc_BMI_category(bmi)

# # print results
print_results(
	name=user_data['name'],
	bmi=bmi,
	bmi_category=bmi_category
)


### EXPECTED OUTPUT
# Enter your name, please: Ada
# I need to know your height in meters: 1.67
# And your weight in kilograms: 56
#
# **************************************************
# Ada, your BMI is 20.08.  Category:  Normal range
# **************************************************