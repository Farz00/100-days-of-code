from art import logo
print(logo)

#add
def add (n1,n2):
    return n1+n2

#Substract
def sub(n1,n2):
    return n1-n2

#multiply
def mul(n1,n2):
    return n1*n2

#Divide
def div(n1,n2):
    return n1/n2

operation = {'+':add, 
             '-':sub,
             '*':mul,
             '/':div}

def calculator():
    cal_cont = True
    n1 = float(input("Enter first value: "))

    for symbol in operation:
        print(symbol)

    while cal_cont == True:
        ops = input("Pick an operation from the line above: ")
        n2 = float(input("Enter second value: "))
        function = operation[ops]
        result = function(n1, n2)

        print(f"{n1} {ops} {n2} = {result}")
        cont = input(f"type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if cont == 'y':
            n1 = result
        else:
            cal_cont = False
            calculator()

calculator()