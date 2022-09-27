from typing import List
from .models.debt_statement import DebtStatement
from .models.participant import Participant, Payer, Lender
from .models.receipt import Receipt
from entities.models import participant
from utils import util


class DebtCalculation:

    def calculate_debt(self, participants: List[Participant], receipts: List[Receipt], default_player_name: str) -> List[DebtStatement]:
        payers: List[Payer] = [x for x in participants if isinstance(x, Payer)]
        lenders: List[Lender] = [x for x in participants if isinstance(x, Lender)]
        default_payer = util.get_participant_by_name(payers, default_player_name)
        
        self.add_receipts_to_participants_balance(participants=participants, receipts=receipts)
        self.add_lenders_balance_to_default_payers(lenders=lenders, default_payer=default_payer)

        total_expenses = self.sum_up_all_expenses(receipts=receipts)
        equal_share = total_expenses / len(payers)
        self.substract_equal_share_from_payers(equal_share=equal_share, payers=payers)

        payers_debt_statements = self.create_payers_debt_statements(payers = payers)
        lenders_debt_statemtns = self.create_lenders_debt_statements(lenders = lenders, default_payer=default_payer)

        return util.concat_two_lists(payers_debt_statements, lenders_debt_statemtns)

    def add_receipts_to_participants_balance(self, receipts: List[Receipt], participants: List[Participant]):
        for receipt in receipts:
            participant = util.get_participant_by_name(participants, receipt.participant_name)
            participant.add_to_balance(receipt.amount)

                
    def sum_up_all_expenses(self, receipts: List[Receipt]) -> float:
        total_balance = 0
        for receipt in receipts:
            total_balance += receipt.amount
        return total_balance

    def substract_equal_share_from_payers(self, payers: List[Payer], equal_share: float):
        for payer in payers:
            payer.substract_of_balance(equal_share)

    def add_lenders_balance_to_default_payers(self, lenders: List[Lender], default_payer: Payer):
        for lender in lenders:
            amount_to_add = lender.balance
            default_payer.add_to_balance(amount_to_add)

    def create_payers_debt_statements(self, payers: List[Payer]) -> List[DebtStatement]:
        debt_statements: List[DebtStatement] = []
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
        return debt_statements

    def create_lenders_debt_statements(self, lenders: List[Lender], default_payer: Payer) -> List[DebtStatement]:
        debt_statements: List[DebtStatement] = []
        for lender in lenders:
            debt_statements.append(DebtStatement(lender, default_payer, lender.balance))
            lender.substract_of_balance(lender.balance)
        return debt_statements


        

