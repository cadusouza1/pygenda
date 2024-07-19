from dataclasses import dataclass
from typing import Tuple

import contact
from exceptions import ContactNotFoundException


@dataclass
class ContactBook:
    contacts: list[contact.Contact]

    def add(self, contact: contact.Contact) -> None:
        self.contacts.append(contact)

    def remove(self, index: int) -> contact.Contact:
        return_val = self.contacts[index]

        del self.contacts[index]
        return return_val

    def search_by_phone(self, phone: str) -> Tuple[int, contact.Contact]:
        for i, contact in enumerate(self.contacts):
            if contact.phone == phone:
                return i, contact

        raise ContactNotFoundException(phone)

    def search_by_name(
        self, name: str
    ) -> Tuple[Tuple[int, contact.Contact], ...]:
        contacts = tuple(
            filter(
                lambda val: val[1].name == name,
                enumerate(self.contacts),
            ),
        )

        if not contacts:
            raise ContactNotFoundException(name)

        return contacts

    def print_all_contacts(self) -> None:
        if not self.contacts:
            print("Contact book is empty")
            return

        for contact in self.contacts:
            print(contact)

    def __iter__(self):
        return iter(self.contacts)

    def __getitem__(self, items):
        return self.contacts[items]
