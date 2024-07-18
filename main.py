import contact
import contact_book
import menu_option


def load_contact_book_from_txt_file(txt: str) -> contact_book.ContactBook:
    with open(txt, "r") as f:
        return contact_book.ContactBook(
            list(
                map(
                    lambda c: contact.Contact(c[0], c[1]),
                    map(
                        lambda line: line.strip().replace("\n", "").split(","),
                        f,
                    ),
                )
            )
        )


def save_contact_book_to_txt_file(
    txt: str, book: contact_book.ContactBook
) -> None:
    with open(txt, "w") as f:
        f.writelines(map(lambda c: f"{c.name},{c.phone}\n", book))


def search_contact_by_phone(
    book: contact_book.ContactBook,
) -> None:
    name = input("Name: ")
    contacts = book.search_by_phone(name)

    if contacts is []:
        print("No contacts found")
        return

    for c in contacts:
        print(c)


def search_contact_by_name(
    book: contact_book.ContactBook,
) -> None:
    name = input("Name: ")
    _, c = book.search_by_name(name)

    if c is None:
        print("Contact not found")
        return

    print(c)


def add_contact(book: contact_book.ContactBook) -> None:
    name = input("Name: ")
    phone = input("Phone: ")

    book.add(contact.Contact(name, phone))


def remove_contact(
    book: contact_book.ContactBook,
) -> contact.Contact | None:
    name = input("Name of the contact to remove: ")
    contacts = book.search_by_name(name)

    if not contacts:
        print("Contact not found")
    else:
        book.remove(contacts[0][0])  # Remove the first contact with the name
        print(f"Contact removed")


def edit_contact(book: contact_book.ContactBook) -> None:
    name = input("Name of the contact to edit: ")
    index, _ = book.search_by_name(name)

    if index == -1:
        print("Contact not found")
        return

    new_name = input("New name (leave blank cancel): ")
    new_phone = input("New phone (leave blank cancel): ")

    if new_name:
        book[index].name = new_name

    if new_phone:
        book[index].phone = new_phone


def main():
    txt = "contacts.txt"
    book = load_contact_book_from_txt_file(txt)
    menu = [
        menu_option.MenuOption("Add", lambda book: add_contact(book)),
        menu_option.MenuOption("Remove", lambda book: remove_contact(book)),
        menu_option.MenuOption("Edit", lambda book: edit_contact(book)),
        menu_option.MenuOption("List", lambda book: book.list_all_contacts()),
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

        if option >= len(menu):
            print("Invalid option")
            continue

        menu[option - 1].fn(book)
        print()

    save_contact_book_to_txt_file(txt, book)


if __name__ == "__main__":
    main()
