from entities.models.participant import Participant
from typing import List, Any

def get_participant_by_name(participants: List[Participant], participant_name: str) -> Participant:
            for participant in participants:
                if(participant.name == participant_name):
                    return participant
            # TODO: Throw appropiate error for when a participant is not present
            raise ValueError()

def concat_two_lists(first: List[Any], second: List[Any]):
    return first + second