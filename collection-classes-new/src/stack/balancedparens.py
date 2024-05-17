from stack.stack import *

class balancedparens:
    @staticmethod
    def isBalanced(expression: str):
        """Checks a specified mathematical expression to see when the
        parenthesis are balanced.

        Args:
            expression (str): specified mathematical expression

        Returns:
            Boolean: True if the parenthesis in the expression are 
            balanced, else False
        """        
        # constants for parenthesis
        LEFT_NORMAL = '('
        RIGHT_NORMAL = ')'
        LEFT_CURLY = '{'
        RIGHT_CURLY = '}'
        LEFT_SQUARE = '['
        RIGHT_SQUARE = ']'

        # stack used to store parenthesis
        store = stack()

        # variable used to indicate an imbalance
        imbalance = False

        # loop through the mathematical expression a character at
        # time as long as there isn't an imbalance 
        for s in expression:
            if(not imbalance):
                if(s == LEFT_CURLY or s == LEFT_NORMAL or s == LEFT_SQUARE):
                    # if the current character is a (, {, or [ 
                    # push it onto the stack
                    store.push(s)
                elif(s == RIGHT_NORMAL):
                    # if the current character is a ), set imbalance to 
                    # true if the stack is empty or the top parenthesis
                    # is not (.
                    if (store.isEmpty() or store.pop() != LEFT_NORMAL):
                        imbalance = True
                elif(s == RIGHT_CURLY):
                    # if the current character is a }, set imbalance to 
                    # true if the stack is empty or the top parenthesis
                    # is not {}.
                    if (store.isEmpty() or store.pop() != LEFT_CURLY):
                        imbalance = True
                elif(s == RIGHT_SQUARE):
                    # if the current character is a ], set imbalance to 
                    # true if the stack is empty or the top parenthesis
                    # is not [.
                    if (store.isEmpty() or store.pop() != LEFT_SQUARE):
                        imbalance = True

        # return true if their are no parenthesis on 
        # the stack and an imbalance is not found
        return (store.isEmpty() and not imbalance)