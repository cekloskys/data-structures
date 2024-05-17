from account.account import *

class savingsaccount(account):
    """The SavingsAccount class has methods to manage the balance
    and interest rate of a savings account.

    Args:
        account (account): class that includes methods to manage the balance
    of a bank account.
    """
    def __init__(self, balance, interestRate):
        """Constructs a savings account with a specified balance and interest rate.

        Args:
            balance (float): balance
            interestRate (float): interest rate
        """
        super().__init__(balance)
        self.__interestRate = interestRate

    def __del__(self):
        """Destroys a specified savings account object and displays message.
        """
        print("Savings account deleted.")

    def getInterest(self):
        """Returns the interest for the calling savings account.

        Returns:
            float: interest
        """
        # return self.__balance * self.__interestRate
        return self.getBalance() * self.__interestRate
    
    def setInterestRate(self, interestRate: float):
        """Sets the interest rate for the calling savings account.

        Args:
            interestRate (float): interest rate
        """
        self.__interestRate = interestRate

    def credit(self, amount: float):
        """Increases the balance of the calling savings account by the specified
        amount times the interest rate of this savings account.

        Args:
            amount (float): the amount to increase the balance by
        """
        super().credit(amount * self.__interestRate)

    def __str__(self):
        """Returns string representation of the calling savings account.

        Returns:
            str: string representation of the calling savings account
        """
        return f"savingsaccount balance={self.getBalance()} interestRate={self.__interestRate}"
    
    def __eq__(self, other):
        """Tests if the calling savings account is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling savings account is equal to the specified
            object, else False
        """
        if other is not None:
            if isinstance(other, savingsaccount):
                if other.getBalance() == self.getBalance():
                    if other.__interestRate == self.__interestRate:
                        return True
        return False