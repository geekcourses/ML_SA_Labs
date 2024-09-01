### Given
#        Product 1 | Product 2 | Avg
# male:    0.6     | 0.4       | 0.5
# female:  0.3     | 0.7       | 0.5
# Avg:     0.45    | 0.55


# Task: write a python program that will calculate the probability that a client is male, given that he choose Product1.

# A - the event that the customer chooses Product1,
# B - the event that the customer is male.

# P(A) - the probability that a customer chooses Product1 = 45% (0.45)
# P(B) - the probability that a customer is male = 50% (0.5)
# P(A|B) - the probability that customer will choose Product1, given that he is male = 60% (0.6)
# P(B|A) - the probability that the customer is male given that they have chosen Product1 =
# P(A and B) - the probability a customer chooses Product1 and to be man =  P(A and B) = P(B) * P(A|B)

# P(B|A) = P(A and B) / P(A)
#        = (P(B) * P(A|B))/P(A)



# def main():
#     pa = 0.45
#     pb = 0.5
#     pab = 0.6

#     pba = (pb*pab)/pa
#     print(f'probability that a client is male, given that he choose Product1: {pba}')


# main()


