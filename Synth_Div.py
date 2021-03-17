# The following program is a CLI application that will allow the user to perofrm a synthetic division on a 
# polynomial of n terms.
import re

def syntheticDivide(terms,divisor):
    answer_list = []
    divisor = divisor * -1
    temp = 0
    temp_2 = 0
    for i in range(len(terms)):
        if i == 0:
            temp = terms[i]
            answer_list.append(temp)
            temp = divisor * terms[i] 
        else:
            temp_2 = temp + terms[i]
            answer_list.append(temp_2)
            temp = temp_2 * divisor
    return answer_list

print('#======================================================================.')
print(' Welcome to the Synthetic Divider by Manuel Argueta!')

while True:
    print('#======================================================================.')
    term_list = []
    print(' ')
    divisorString = str(input(' Please enter the divisor: '))
    divisorList = [int(d) for d in re.findall(r'-?\d+', divisorString)]
    divisor = divisorList[0]
    terms = int(input(' Please enter the number of terms in polynomial in the dividend: '))
    for i in range(terms):
        newTerm = int(input(' Please enter the coefficent of term ' + str(i + 1) + ' of the polynomial being divided: '))
        term_list.append(newTerm)
    answers = syntheticDivide(term_list, divisor)
    power = len(answers)-2
    print(' ')
    op = ''
    print('#======================================================================.')
    print(' Your Solution: ')
    for i in range(len(answers)):
        if i < len(answers)-2:
            if answers[i+1] > 0:
                op = ' + '
            elif answers[i+1] < 0: 
                op = ' '
        if i == len(answers)-1 and answers[i] != 0:
            print('Remainder: ' + str(answers[i]) + '/ x + ' + str(divisor))
            break
        elif i == len(answers)-1 and answers[i] == 0:
            print('Remainder: ' + str(answers[i]))
            break
        if power >= 2:
            if answers[i] == 1:
                print(' x^' + str(power) + op , end = '')
            elif answers[i] != 1:
                print(str(answers[i]) + 'x^' + str(power) + op, end = '')
        elif power == 1: 
            if answers[i] == 1:
                print('x' + op, end = '')
            elif answers[i] != 1:
                print(str(answers[i]) + 'x' + op, end = '')
        else:
            print(str(answers[i]) + ' ', end = '')
        power -=1
        if answers[i] > 0:
            op = ' + '
        elif answers[i] < 0: 
            op = ' '
    print()
    print('#======================================================================.')
    res = input(' Enter Another Problem?...(y/n): ' )
    if res != 'y':
        print('#======================================================================.')
        print(' Thanks for using this Synthetic Divider by Manuel Argueta!')
        print('#======================================================================.')
        break