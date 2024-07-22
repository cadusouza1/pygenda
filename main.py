import contact
import contact_book
import menu_option
import validation
from exceptions import (ContactNotFoundException,
                        DuplicatedPhoneNumberException, InvalidNameException,
                        InvalidPhoneNumberException)


def load_contact_book_from_txt_file(txt: str) -> contact_book.ContactBook:
    try:
        with open(txt, "r") as f:
            return contact_book.ContactBook(
                list(
                    map(
                        lambda c: contact.Contact(c[0], c[1]),
                        map(
                            lambda line: line.strip()
                            .replace("\n", "")
                            .split(","),
                            f,
                        ),
                    )
                )
            )
    except FileNotFoundError:
        return contact_book.ContactBook([])


def save_contact_book_to_txt_file(
    txt: str, book: contact_book.ContactBook
) -> None:
    with open(txt, "w") as f:
        f.writelines(map(lambda c: f"{c.name},{c.phone}\n", book))


def search_contact_by_phone(
    book: contact_book.ContactBook,
) -> None:
    try:
        phone = input("Phone: ")
        validation.validade_contact_phone(phone)
        _, c = book.search_by_phone(phone)
        print(c)
    except (ContactNotFoundException, InvalidPhoneNumberException) as e:
        print(e)


def search_contact_by_name(
    book: contact_book.ContactBook,
) -> None:
    try:
        name = input("Name: ")
        validation.validade_contact_name(name)

        for _, c in book.search_by_name(name):
            print(c)
    except (InvalidNameException, ContactNotFoundException) as e:
        print(e)


def add_contact(book: contact_book.ContactBook) -> None:
    try:
        name = input("Name: ")
        validation.validade_contact_name(name)

        phone = input("Phone: ")
        validation.validade_contact_phone(phone)

        if any(filter(lambda c: phone == c.phone, book)):
            raise DuplicatedPhoneNumberException(phone)

        book.add(contact.Contact(name, phone))
    except (
        InvalidNameException,
        InvalidPhoneNumberException,
        DuplicatedPhoneNumberException,
    ) as e:
        print(e)


def remove_contact(
    book: contact_book.ContactBook,
) -> contact.Contact | None:
    try:
        name = input("Name of the contact to remove: ")
        validation.validade_contact_name(name)

        contacts = book.search_by_name(name)
        removed = book.remove(contacts[0][0])
        print(f'Contact "{removed.name}" removed')
    except (ContactNotFoundException, InvalidNameException) as e:
        print(e)


def edit_contact(book: contact_book.ContactBook) -> None:
    try:
        name = input("Name of the contact to edit: ")
        validation.validade_contact_name(name)
        index, _ = book.search_by_name(name)
    except (ContactNotFoundException, InvalidNameException) as e:
        print(e)
        return

    new_name = input("New name (leave blank cancel): ")
    new_phone = input("New phone (leave blank cancel): ")

    if new_name:
        book[index].name = new_name

    if new_phone:
        try:
            validation.validade_contact_phone(new_phone)
            book[index].phone = new_phone
        except InvalidPhoneNumberException as e:
            print(e)
            return


def main():
    txt = "contacts.txt"
    book = load_contact_book_from_txt_file(txt)
    menu = [
        menu_option.MenuOption("Add", lambda book: add_contact(book)),
        menu_option.MenuOption("Remove", lambda book: remove_contact(book)),
        menu_option.MenuOption("Edit", lambda book: edit_contact(book)),
        menu_option.MenuOption("List", lambda book: book.print_all_contacts()),
        menu_option.MenuOption(
            "Search by name", lambda book: search_contact_by_name(book)
        ),
        menu_option.MenuOption(
            "Search by phone", lambda book: search_contact_by_phone(book)
        ),
    ]

    while 1:
        print("Select an option (0 to stop): ")
        for i, m in enumerate(menu):
            print(f"{i + 1}. {m.label}")

        option = input("Enter your option: ")

        if not option.isnumeric():
            print("Invalid input. Please input a valid option\n")
            continue

        option = int(option)
        print()

        if option == 0:
            break

        if option > len(menu):
            print("Invalid option")
            continue

        menu[option - 1].fn(book)
        print()

    save_contact_book_to_txt_file(txt, book)


if __name__ == "__main__":
    main()
