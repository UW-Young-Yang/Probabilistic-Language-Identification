import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=[0]*26
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here
        for line in f:
            line = line.strip().upper()
            for char in line:
                asc_char = ord(char)-ord('A')
                if 0 <= asc_char <= 25:
                    X[asc_char] += 1

    return X



# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!

def sum_cal(X, language): 
    res = 0
    for i in range(26):
        res += X[i] * math.log(language[i])
    return res

def Q1(X):
    print('Q1')
    for i in range(26):
        print(chr(ord('A')+i), X[i])

def Q2(X, prob_table):
    e, s = prob_table
    formula1 = X[0] * math.log(e[0])
    formula2 = X[0] * math.log(s[0])
    print('Q2')
    print('%.4f' % formula1)
    print('%.4f' % formula2)

def Q3(X, prob_table):
    prob_english = 0.6
    prob_spanish = 1 - prob_english
    english = math.log(prob_english) + sum_cal(X, prob_table[0])
    spanish = math.log(prob_spanish) + sum_cal(X, prob_table[1])
    print('Q3')
    print(f'{english:.4f}')
    print(f'{spanish:.4f}')
    return english, spanish

def Q4(F_func):
    english, spanish = F_func
    diff = spanish - english
    if diff  >= 100:
        res = 0
    elif diff <= -100:
        res = 1
    else:
        res = 1 / (1 + math.e**diff)
    print('Q4')
    print('%.4f' % res)

if __name__ == '__main__':
    X = shred('letter.txt')
    prob_table = get_parameter_vectors()
    Q1(X)
    Q2(X, prob_table)
    F_func = Q3(X, prob_table)
    Q4(F_func)