from account.account import *
from savingsaccount.savingsaccount import *

def main():
    # create an account object named a1 and initialize
    # its balance to $100
    a1 = account(100.0)
    # a1 = account(100.0, 200.0, 300.0, 400.0)
    # a1 = account(-100.0) a balance less than zero will result in our code raising a ValueError

    print(a1)
    # print(a1.public) # referencing a public instance variable will not result in an error
    # print(a1.__balance) # referencing a private instance variable will result in an error
    # print(a1._account__balance) # referencing a private instance variable will not result in an error when 
    # when the variable is prefixed with the name of the class
    # print(a1._protected) # referencing a protected instance variable will not result in an error

    # a1.__privateMethod() # referencing a private method will result in an error
    # a1._account__privateMethod() # referencing a private method will not result in an error when
    # the method is prefeixed with the name of the class
    # a1._protectedMethod() # referencing a protected method will not result in an error
    # a1.publicMethod() # referencing a public method will not result in an error

    # Display the balance of a1
    print("$%.2f" % (a1.getBalance()))

    # Increase the balance of a1 by $50
    a1.credit(50.0)
    # a1.credit(-50) a credit amount less than zero will result in our code raising a ValueError

    # Display the balance of a1
    print("$%.2f" % (a1.getBalance()))

    # Decrease the balance of a1 by $75
    a1.debit(75.0)
    # a1.debit(-75.0) a debit amount less than zero will result in our code raising a ValueError
    # a1.debit(750.0) a debit amount greater than the balance will result in our code raising a ValueError

    # Display the balance of a1
    print("$%.2f" % (a1.getBalance()))

    # Display if the balance for a1 is empty
    print('Is account balance empty?', a1.isEmpty())

    # Create a second Account object named a2 and initialize
    # its balance to $0
    a2 = account()

    # Display the balance of a2
    print("$%.2f" % (a2.getBalance()))

    # Increase the balance of a2 by $50
    a2.credit(50.0)
    
    # Display the balance of a2
    print("$%.2f" % (a2.getBalance()))

    # Decrease the balance of a2 by $75
    a2.debit(25.0)

    # Display the balance of a2
    print("$%.2f" % (a2.getBalance()))

    # Display if the balance for a2 is empty
    print('Is account balance empty?', a2.isEmpty())

    # Display a String representation of a1 and a2
    print(a1)
    print(a2)

    # Create a third account object named a3 and 
    # initialize it to None
    a3 = None

    # Display the result of testing if a1 is equal to a3    
    print(a1.__eq__(a3))

    # Create a string named s1 and initialize it to I love Python
    s1 = 'I love Python'

    # Display the result of testing if a1 is equal to s1    
    print(a1.__eq__(s1))

    # Increase the balance of a2 by $50
    a2.credit(50.0)

    # Display the result of testing if a1 is equal to a2    
    print(a1.__eq__(a2))

    # Display the sum of the balances in a1 and a2
    print("$%.2f" % account.sum(a1, a2))

    # Display the sum of the balances in a1 and a3
    # print("$%.2f" % account.sum(a1, a3))

    # Display the sum of the balances in a1 and s1
    print("$%.2f" % account.sum(a1, s1))

    # Transfer $25 from a1 into an account named a4
    a4 = account.transfer(a1, 50)
    # a4 = account.transfer(a3, 50)
    # a4 = account.transfer(a1, -50)
    # a4 = account.transfer(a1, 1500)
    # a4 = account.transfer(s1, 50.0)

    # Display the balance of a4
    print("$%.2f" % (a4.getBalance()))
    
    # Display the balance of a1
    print("$%.2f" % (a1.getBalance()))

    # Create a savings account object named sa1 and initialize
    # its balance to $10000 and its interest rate to 6%
    sa1 = savingsaccount(10000.0, 0.06)

    # Display the balance of sa1
    print("$%.2f" % (sa1.getBalance()))

    # Display the interest of sa1
    print("$%.2f" % (sa1.getInterest()))

    # Display if the balance for sa1 is empty
    print('Is account balance empty?', sa1.isEmpty())

    # Display a String representation of sa1
    print(sa1)

    # Display the result of testing if sa1 is equal to a2
    print(sa1.__eq__(a2))

    # Display the result of testing if sa1 is equal to a3
    print(sa1.__eq__(a3))

    # Create a savings account object named sa2 and initialize
    # its balance to $10000 and its interest rate to 5%
    sa2 = savingsaccount(10000.0, 0.05)

    # Display the result of testing if sa1 is equal to sa2
    print(sa1.__eq__(sa2))

    # Change the interest rate of sa2 to 6%
    sa2.setInterestRate(.06)

    # Display the result of testing if sa1 is equal to sa2
    print(sa1.__eq__(sa2))

if __name__ == "__main__":
    main()