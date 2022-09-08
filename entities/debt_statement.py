
from typing import List
from . import participant

class DebtStatement:

    def __init__(self, lender: participant.Participant, borrower: participant.Participant,  amount: float) -> None:
        self.lender = lender
        self.borrower = borrower
        self.amount = amount

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, DebtStatement) and obj.lender == self.lender and obj.borrower == self.borrower and obj.amount == self.amount