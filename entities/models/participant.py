from abc import ABC, abstractmethod
from typing import List

class Participant(ABC):
        balance: float = 0

        def __init__(self, name: str) -> None:
             self.name = name

        def add_to_balance(self, amount: float) -> None:
         self.balance += amount
        
        def substract_of_balance(self, amount: float) -> None:
            self.balance -= amount

        @abstractmethod
        def __eq__(self, __o: object) -> bool:
             pass


class Payer(Participant):
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Payer) and self.name == __o.name and self.balance == __o.balance


class Lender(Participant):

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Lender) and self.name == __o.name and self.balance == __o.balance
