from typing import List
from ..models.participant import Lender, Participant, Payer
from ..debt_calculation import DebtCalculation
from ..models.debt_statement import DebtStatement
from ..models.receipt import Receipt

def test_calculate_debt_statements():
    participants: List[Participant] = [Payer("Markus"), Payer("Max"), Lender("Annso")]
    receipts: List[Receipt] = [Receipt(100, participant_name = "Max"), Receipt(200, participant_name = "Markus"), Receipt(20, participant_name="Annso")]
    result = DebtCalculation().calculate_debt(participants, receipts, default_player_name="Markus")
    annso_debt_statement = DebtStatement(lender=participants[2], borrower=participants[0], amount=20)
    markus_debt_statement = DebtStatement(lender=participants[0], borrower=participants[1], amount=60)
    expected = [markus_debt_statement, annso_debt_statement]
    assert result == expected


def test_add_lenders_balance_to_default_payers():
    default_payer: Payer = Payer(name="Markus")
    lenders: List[Lender] = [Lender(name="Max")]
    lenders[0].add_to_balance(100)
    DebtCalculation().add_lenders_balance_to_default_payers(lenders=lenders, default_payer=default_payer)
    assert default_payer.balance == 100

# test create_payers_debt_statements
def test_create_payers_debt_statements():
    payer_markus = Payer(name="Markus")
    payer_markus.add_to_balance(50)
    payer_max = Payer(name="Max")
    payer_max.substract_of_balance(50)
    payers: List[Payer] = [payer_markus, payer_max]
    expected: List[DebtStatement] = [DebtStatement(lender=payer_markus, borrower=payer_max, amount=50)]
    result = DebtCalculation().create_payers_debt_statements(payers=payers)
    assert expected == result

# test create_lenders_debt_statements
def test_create_lenders_debt_statements():
    payer_markus = Payer(name="Markus")
    lender_annso = Lender(name="Annso")
    lender_annso.add_to_balance(100)
    expected: List[DebtStatement] = [DebtStatement(lender=lender_annso, borrower=payer_markus, amount=100)]
    result = DebtCalculation().create_lenders_debt_statements(lenders=[lender_annso], default_payer=payer_markus)
    assert expected == result
