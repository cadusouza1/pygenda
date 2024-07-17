import contact
import contact_book


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
    index, _ = book.search_by_name(name)

    if index == -1:
        print("Contact not found")
    else:
        book.remove(index)
        print("Contact removed")


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

    while 1:
        print("Select an option: ")
        print("1. Add")
        print("2. Remove")
        print("3. Edit")
        print("4. List")
        print("5. Search by name")
        print("6. Search by phone")
        print("7. Stop")

        option = int(input("Enter your option: "))
        print()

        if option == 1:
            add_contact(book)
        elif option == 2:
            remove_contact(book)
        elif option == 3:
            edit_contact(book)
        elif option == 4:
            book.list_all_contacts()
        elif option == 5:
            search_contact_by_name(book)
        elif option == 6:
            search_contact_by_phone(book)
        elif option == 7:
            break
        else:
            print("Invalid option")

        print()

    save_contact_book_to_txt_file(txt, book)


if __name__ == "__main__":
    main()
