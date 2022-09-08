from typing import List
from .debt_statement import DebtStatement
from .participant import Participant, Payer, Lender
from .receipt import Receipt


class DebtCalculation:

    def __init__(self, receipts: List[Receipt], participants: List[Participant]):
        self.receipts = receipts
        self.participants = participants

    def calculate_debt(self) -> List[DebtStatement]:
        total_balance = 0

        # Should probbaly be its own function
        for receipt in self.receipts:
            if(receipt.participant in self.participants):
                total_balance += receipt.amount
                receipt.participant.add_to_balance(receipt.amount)
            else:
                raise ValueError

        payers: List[Payer] = [x for x in self.participants if isinstance(x, Payer)]
        equal_share = total_balance / len(payers)

        # calculate who owns who what
        for payer in payers:
            payer.substract_of_balance(equal_share)

           
        debt_statements: List[DebtStatement] = []
        # create debt statements for payers
        for payer_a in payers:
            if (payer_a.balance > 0):
                for payer_b in payers:
                    if(payer_b.balance < 0):
                        debt_to_pay = min(abs(payer_b.balance), payer_a.balance)
                        debt_statements.append(DebtStatement(payer_a, payer_b, debt_to_pay))
                        payer_a.substract_of_balance(debt_to_pay)
                        payer_b.add_to_balance(debt_to_pay)
                        if(payer_a.balance == 0):
                            break


        # add debtStatements for lenders
        lenders: List[Lender] = [x for x in self.participants if isinstance(x, Lender)]
        for lender in lenders:
            debt_statements.append(DebtStatement(lender, lender.default_payer, lender.balance))
                            
        return debt_statements
                            

            


        

