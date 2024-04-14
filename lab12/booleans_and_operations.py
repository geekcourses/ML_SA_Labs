# print(2)
# print('true')
# print(True)

# int=> how many different values are? (1,2, -1, 0, 19982943) => infinit


# user_age = 15
# if user_age>=18:
#     print('Welcome')
# else:
#     print('You can not use my program')


# user_name = ''

# if user_name:
#     print(f'Welcome {user_name}')
# else:
#     print('Welcome, Anonymous')


# print( bool(3) )
# print( bool(0) )


# --------------------------- Comparison Operators --------------------------- #
# print( 5==5 )
# print( 5!=5 )
# print( 5>=5 )
# print( 5>5 )
# print( 5>='5' ) # Error

# print( 9 < 1000)        #True
# print( "9"<"1000" )     #False
# print( "9"<"1" )
# print( 57<49 )

# print( ord('9') )



#TASK:
# User enter a number
# Print if number is in [1..10]

# x = int( input('x=') )
# print( 1<=x<=10 )


# ----------------------------- Logical Operators ---------------------------- #
# print( True and True ) # T
# print( True and False ) # F
# print( True or False) # T
# print( not False)    # T


# user_age = 19
# user_country = 'UK'

# # Task: print 'Welcome' if user is adult and user is from 'UK'
# if user_age>=18 and user_country=='UK':
#     print('Welcome')


# print( 4 or 0 ) #4
# print( 4 and 0 ) #0
# print( not 0 ) #T


# print( 4 or 874358743*6743 )
# print( 0 or 874358743*6743 )

# print( bool(0) )
# print( 0 and 2-4*54 )

# user_name = ''

# user_name = user_name or 'Anonymous'

# print(user_name)


# -------------------------- Control Flow Statements ------------------------- #
# x=-5
# if x>0:
#     print('Positive')
#     print('++++')


# print( bool(-1) )
# if -1:
#     print('hi')


# x = 9

# if x%2==0:
#     print('Even')
# else:
#     print('Odd')


# TASK:
# if x==0 => 'Zero'
# if x==100 => '100'
# if x is even => 'Even'
# if x is odd => 'odd'

### Variant 1: nested if - else (NOT GOOD)
# x = 100

# if x==0:
#     print('Zero')
# else:
#     if x==100:
#         print('100')
#     else:
#         if x%2==0:
#             print('Even')
#         else:
#             print('Odd')

### Variant 2: if -elif - else  (GOOD)
# x = 102
# if x==0:
#     print('Zero')
# elif x==100:
#     print('100')
# elif x%2==0:
#     print('Even')
# else:
#     print('Odd')


# --------------------------------- Examples --------------------------------- #

# Scenario: Automated Coffee Order Assistant

# Problem: You love freshly brewed coffee, but deciding what to order often depends on factors like the time of day, how tired you feel, and whether you want something hot or cold.  Let's build a Python program to help streamline your coffee choices!


time_of_day = input("What time of day is it (morning, afternoon, evening)? ").lower()
energy_level = input("How tired are you feeling (low, medium, high)? ").lower()
temperature = input("Do you want a hot or cold drink? ").lower()

if time_of_day == "morning":
    if energy_level == "low":
        print("You need a boost! I recommend a double espresso.")
    else:
        print("A classic latte should do the trick.")

elif time_of_day == "afternoon":
    if temperature == "hot":
        print("Try a refreshing iced coffee.")
    else:
        if energy_level == "low":
            print("A cold brew with a shot of espresso might be perfect.")
        else:
            print("A light cappuccino sounds lovely!")

else:  # It's evening
    if energy_level in ["medium", "high"]:
        print("Enjoy a decaf latte to relax.")
    else:
        print("Herbal tea is a better choice for this time of day.")
