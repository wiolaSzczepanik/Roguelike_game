import random

def choose_number():
    count = 0
    digit_list = []

    while count < 3:
        digit = random.randint(0,9)
        if digit in digit_list:
            continue
        else:
            digit_list.append(str(digit))
            count += 1
    print(digit_list)
    return digit_list

def input_user():

    while True:
        number = input("Pick a number: ")
        try:
            int(number)
            if len(number) != 3:
                raise ValueError
        except ValueError:
            print("Input has to be tree digits integer. Try again.")
        else:
            break

    return number

def compar_numbers(digit_list, digit_number):
    hot = 0
    warm = 0

    for i in range(len(digit_list)):
        if digit_list[i] == digit_number[i]:
            hot += 1
            print("hot")
    for i in range(len(digit_list)):
        if digit_list[i] == digit_number[i]:
            continue
        elif digit_number[i] in digit_list:
            warm += 1
            print("warm")

    if hot == 3:
        pass
    elif warm == 0 and hot == 0:
        print("Cold")

    return hot


def main():
    digit_list = choose_number()
    while True:
        digit_number = input_user()
        hot = compar_numbers(digit_list, digit_number)
        if hot == 3:
            print("Win")
            break
