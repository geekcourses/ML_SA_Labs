# In a school yard there are 40 girls and 60 boys. All of the boys wear trousers, half of the girls wear trousers, and the other half - wear skirts.
# An observer sees a student from a distance, but she can only see that this student wears trousers.
# What is the probability that student to be a girl?

Given:
        Gender | Number of students | Students with trousers
         girl  |             40     |                  20
         boy   |             60     |                  60
        Total: |             100    |                  80

    G - event that a student is a girl
    T - event that a student wears trousers

Solution:
    1. With Conditional Probability Formula:
        P(G|T) =  P(G and T) / P(T)


        P(T)        = 80/100 = 0.8
        P(G)        = 40/100 = 0.4
        P(G and T)  = 20/100 = 0.2

        P(G|T) =  0.2/0.8 = 0.25

    2. With Bayes' Theorem:
        P(G|T) = P(T|G) * P(G) / P(T)

        P(T|G) = 20/40 = 0.5

        P(G|T) = 0.5 * 0.4 / 0.8 = 0.25

