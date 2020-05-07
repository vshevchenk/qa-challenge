from attr import dataclass


@dataclass
class Credentials:
    email: str
    password: str
