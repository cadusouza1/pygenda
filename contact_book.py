from dataclasses import dataclass
from typing import Tuple

import contact


@dataclass
class ContactBook:
    contacts: list[contact.Contact]

    def add(self, contact: contact.Contact) -> None:
        self.contacts.append(contact)

    def remove(self, index: int) -> contact.Contact:
        return_val = self.contacts[index]

        del self.contacts[index]
        return return_val

    def search_by_name(
        self, contact_name: str
    ) -> Tuple[int, contact.Contact | None]:
        for i, contact in enumerate(self.contacts):
            if contact.name == contact_name:
                return i, contact

        return -1, None

    def search_by_phone(
        self, contact_phone: str
    ) -> list[Tuple[int, contact.Contact]]:
        return list(
            filter(
                lambda val: val[1].phone == contact_phone,
                enumerate(self.contacts),
            ),
        )

    def list_all_contacts(self) -> None:
        for contact in self.contacts:
            print(contact)

    def __iter__(self):
        return iter(self.contacts)

    def __getitem__(self, items):
        return self.contacts[items]
