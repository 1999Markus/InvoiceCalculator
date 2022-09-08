
#from ..debt_statement import DebtStatement
#from ..participant import Participant, Lender, Payer
#from ..receipt import Receipt
from typing import List
import pytest
from entities.participant import Participant, Payer
from entities.debt_calculation import DebtCalculation
from entities.debt_statement import DebtStatement
from entities.receipt import Receipt

def test_calculate_debt_statements():
    participants: List[Participant] = [Payer(name="Markus"), Payer(name="Annso")]
    receipts = [Receipt(amount=100, participant=participants[0])]
    result = DebtCalculation(participants=participants, receipts=receipts).calculate_debt()
    expected = [DebtStatement(participants[0], participants[1], 50)]
    assert expected == result