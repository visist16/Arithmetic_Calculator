import re


def arithmetic_arranger(problems,solve = False):
    #this
    #["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

     #into this 
    #"    3    3801     45     123\n+ 855    -   2  +  43  + 49\n----  ------   ----    ----"
    if(len(problems) > 5):
        return "Error: Too many problems." 
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    for problem in problems :
        if(re.search("[^\s0-9.+-]", problem)) :
            if(re.search("[/]", problem) or re.search("[*]", problem)) :
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        if(len(firstNumber) > 4 or len(secondNumber) > 4):
            return "Error: Numbers cannot be more than four digits."

        sum = ""
        if (operator == "+" ):
            sum = str(int(firstNumber) + int(secondNumber))
        elif (operator == "-"):
            sum = str(int(firstNumber) - int(secondNumber))

        length = max(len(firstNumber), len(secondNumber))
        top = str(firstNumber).rjust(length + 2)
        bottom = operator +" " + str(secondNumber).rjust(length)
        line = ""
        res = sum.rjust(length + 2)
        for s in range(length + 2):
            line += "-"

        

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string
