from abc import ABC, abstractmethod

class Participant(ABC):
        balance: float = 0

        def __init__(self, name: str) -> None:
             self.name = name

        @abstractmethod
        def add_to_balance(amount: float) -> None:
            pass
        
        @abstractmethod
        def __eq__(self, __o: object) -> bool:
             pass


class Payer(Participant):
    
    def add_to_balance(self, amount: float) -> None:
         self.balance += amount
    
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Payer) and self.name == __o.name and self.balance == __o.balance

    def substract_of_balance(self, amount: float) -> None:
        self.balance -= amount


class Lender(Participant):

    def __init__(self, name: str, default_payer: Payer):
        super().__init__(name=name)
        self.default_payer = default_payer

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Lender) and self.name == __o.name and self.balance == __o.balance

    def add_to_balance(self, amount: float) -> None:
         self.balance += amount
         self.default_payer.balance += amount
