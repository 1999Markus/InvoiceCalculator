from . import participant

class Receipt:

    def __init__(self, amount: float, participant: participant.Participant) -> None:
        self.amount = amount
        self.participant = participant