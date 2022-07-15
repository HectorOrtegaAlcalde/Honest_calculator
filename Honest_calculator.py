#-------------------------------------------------------------------------------
# Name:        Honest calculator
# Purpose:
#
# Author:      Hector
#
# Created:     15/07/2022
# Copyright:   (c) Hector 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

msg = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
 "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
 "Yeah... division by zero. Smart move...", "Do you want to store the result? (y / n):",
 "Do you want to continue calculations? (y / n):",
 " ... lazy", " ... very lazy", " ... very, very lazy",
 "You are", "Are you sure? It is only one digit! (y / n)",
 "Don't be silly! It's just one number! Add to the memory? (y / n)",
 "Last chance! Do you really want to embarrass yourself? (y / n)"]

def is_one_digit(v):
    if v.is_integer() and v > -10 and v < 10:
        return True
    else:
        return False

def check(v1, v2, v3):
    msg_ = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg_ = msg_ + msg[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg_ = msg_ + msg[7]
    if (v1 == 0 or v2 == 0) and (v3 == "-" or v3 == "*" or v3 == "+"):
        msg_ = msg_ + msg[8]
    if msg_ != "":
        msg_ = msg[9] + msg_
        print(msg_)

memory = 0

while True:
    print(msg[0])
    calc = input()
    comp = calc.split()
    x, oper, y = comp[0], comp[1], comp[2]
    try:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg[1])
    else:
        if oper == "+" or oper == "-" or oper == "/" or oper == "*":
            check(x, y, oper)
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/":
                try:
                    x / y
                except ZeroDivisionError:
                    print(msg[3])
                    continue
                else:
                    result = x / y
        else:
            print(msg[2])
            break
        print(result)
        while True:
            print(msg[4])
            ans = input()
            if ans.lower() != "y" and ans.lower() != "n":
                continue
            else:
                break
        if ans.lower() == "y":
            if is_one_digit(result):
                msg_index = 10
                while msg_index <= 12:
                    print(msg[msg_index])
                    ans = input()
                    if ans.lower() == "y":
                        msg_index = msg_index + 1
                    elif ans.lower() == "n":
                        break
                    else:
                        continue
                if msg_index == 13:
                    memory = result
            else:
                memory = result
        while True:
            print(msg[5])
            ans = input()
            if ans.lower() != "y" and ans.lower() != "n":
                continue
            else:
                break
        if ans == "y":
            continue
        else:
            break
