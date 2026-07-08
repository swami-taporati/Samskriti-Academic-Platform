from dataclasses import dataclass

@dataclass
class TimetableRequest:
    division:str
    level:str
    term:str
