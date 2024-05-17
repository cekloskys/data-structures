from stack.stack import *

class calculator:  
    @staticmethod
    def evaluate(expression: str):
        """Evaluates a specified mathematical expression.

        Args:
            expression (str): specified mathematical expression

        Returns:
            float: the result of the mathematical expression
        """    
        # stack to store numbers    
        numbers = stack()
        # stack to store operations
        operations = stack()

        # loop through the mathematical expression a character at time
        for s in expression:
            # if current character is a number
            if (s.isnumeric()):
                # push it onto the numbers stack
                numbers.push(float(s))
            else:
                # if the current character is a valid operation
                if (s == '+' or s == '-' or s == '*' or s == '/'):
                    # push it onto the operations stack
                    operations.push(s)
                elif(s == ')'):
                    # if the current character is a right parenthesis
                    # evaluate the stacks
                    calculator.evaluateStackTops(numbers, operations)
                elif(s != '('):
                    # exit if the current character is invalid
                    exit("Illegal input expression!")

        # exit if the numbers stack doesn't have one element
        if (numbers.size() != 1):
            exit("Illegal input expression!")

        # return the element at the top of the numbers stack
        return numbers.pop()
    
    @staticmethod
    def evaluateStackTops(numbers, operations):
        """Applies an operation taken from the specified operations stack to 
        two numbers taken from the specified numbers stack.

        Args:
            numbers (_type_): specified numbers stack
            operations (_type_): specified operations stack
        """   
        # exit if the numbers stack has less than two elements or
        # the operations stack is empty     
        if ((numbers.size() < 2) or (operations.isEmpty())):
            exit("Illegal input expression!")

        # assign the element at the top of the numbers stack to operand2
        operand2 = numbers.pop()
        # assign the element at the top of the numbers stack to operand1
        operand1 = numbers.pop()

        # assign the element at the top of the operations stack to operator
        operator = operations.pop()

        if (operator == '+'):
            # if the operator is +, add operand1 and operand2
            # and push the result onto the numbers stack
            numbers.push(operand1 + operand2)
        elif (operator == '-'):
            # if the operator is -, subtract operand2 from operand1
            # and push the result onto the numbers stack
            numbers.push(operand1 - operand2)
        elif (operator == '*'):
            # if the operator is *, multiply operand1 and operand2
            # and push the result onto the numbers stack
            numbers.push(operand1 * operand2)
        elif (operator == '/'):
            # if the operator is /, divide operand2 by operand1
            # and push the result onto the numbers stack
            numbers.push(operand1 / operand2) 
        else:
             # exit if the operator isn't valid
             exit("Illegal input expression!")