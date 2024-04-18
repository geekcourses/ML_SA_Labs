# -------------------------------- While loop -------------------------------- #
# # example 1 => the use case for while
# x = int(input('Enter even number:'))
# while x%2:
#     x = int(input('Enter even number:'))

# print(x)

# # example 2: => not good for while
# i = 1
# while i<=10 :
#     print(i)
#     i += 1

# print('Enf of loop')
# print(i)

# # 1,2,3,4,5?


# example 3 => not good for while
# 1,2,3,4,5
# i = 1
# total_sum = 0
# while i<=5:
#     # total_sum=total_sum+i
#     total_sum+=i
#     i+=1

# print("total_sum = ", total_sum)

# print( sum(range(1,6)) )

# --------------------------------- For loop --------------------------------- #
# for item in [1,2,3,4,5] :
#     print(item)

# print('END')

# # for l in 'abc':
# #     print(l)

# for item in range(1,6):
#     print(item)

# print('END')



# iterate with indexes - variant 1
# test_str = 'abcd'
# # print( len(test_str) )
# # print( test_str[0] )

# for i in range(0,len(test_str)):
#     print(test_str[i]+str(i))


# test_str = 'abcd'
# for i, l in enumerate(test_str):
#     print(l + str(i))

# a0
# b1
# c2
# d3



# -------------------------------- break loop -------------------------------- #
# while True:
#     x = int(input('Enter even number:'))
#     if x%2==0:
#         break

# Task: 1 .. 10, but when x == 5
# x = 8
# for num in [1,2,3,4,5,6,7,8,9,10]:
#     if num==x:
#         break
#     print(num)


# print('End')

# TASK: print('Found') if target is in fruits, else print('Not found')
# fruits  = ["apple", "banana", "cherry"]
# target = "cherry"
# found = False

# for fruit in fruits:
#     if fruit==target:
#         print('Found')
#         found = True
#         break

# if not found:
#     print('Not found')

# TASK:

# # print program menu:
# print("1. Action 1")
# print("2. Action 3")
# print("3. Action 3")
# while True:
#     user_choice = int(input("Select an action [1,2,3]:"))
#     if user_choice==1:
#         print('Action1')
#         break
#     elif user_choice==2:
#         print('Action2')
#         break
#     elif user_choice==3:
#         print('Action3')
#         break
#     else:
#         print('Wrong input')


# --------------------------------- Contunue --------------------------------- #
# x = 5
# for num in [1,2,3,4,5,6,7,8,9,10]:
#     if num==x:
#         continue
#     print(num)

# print('end')