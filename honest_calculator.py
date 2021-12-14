from operator import add, sub, mul, truediv
messages = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)",
]
operations = {"+": add, "-": sub, "*": mul, "/": truediv}
memory = 0.0

def is_one_digit(v):
    if (-10.0 < v < 10.0) and v.is_integer() is True:
        return True
    else: 
        return False

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + messages[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + messages[7]
    if (v1 == 0 or v2 == 0) and v3 in ["*", "+", "-"]:
        msg = msg + messages[8]
    if msg != "":
        msg = messages[9] + msg
        print(msg)

while True:
    print(messages[0])
    calc = input()
    equation = calc.split()
    x, oper, y = equation[0], equation[1], equation[2]
    if x == "M":
        x = memory
    if y == "M":
        y = memory 
    try: 
        x = float(x)
        y = float(y)
    except ValueError:
        print(messages[1])
        continue 
    else: 
        if oper in operations:
            check(x, y, oper)
            try:
                result = operations[oper](x, y)
                print(result)
                print(messages[4])
                answer = input()
                if answer == "y":
                    if is_one_digit(result) is True:
                        messages_index = 10
                        while messages_index < 13:
                            print(messages[messages_index])
                            answer3 = input()
                            if answer3 == "y":
                                messages_index += 1
                            else:
                                break 
                        if answer3 == "n":
                            print(messages[5])
                            answer2 = input()
                            if answer2 == "y":
                                continue
                            else:
                                break
                        else:
                            memory = result
                            print(messages[5])
                            answer2 = input()
                            if answer2 == "y":
                                continue                        
                            else: 
                                break       
                    else:
                        memory = result  
                        print(messages[5])
                else: 
                    print(messages[5])
                answer2 = input()
                if answer2 == "y":
                    continue
                else:                    
                    break 
            except ZeroDivisionError:
                print(messages[3])
                continue 
        else:
            print(messages[2])  

    
    


