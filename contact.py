from dataclasses import dataclass


@dataclass
class Contact:
    name: str
    phone: str

    def __repr__(self) -> str:
        return f"Name: {self.name}\t| Phone: {self.phone}"
