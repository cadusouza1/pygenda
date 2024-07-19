class InvalidNameException(Exception):
    def __init__(self, name) -> None:
        super().__init__(f"Invalid name {name}")


class InvalidPhoneNumberException(Exception):
    def __init__(self, phone) -> None:
        super().__init__(f"Invalid phone number {phone}")


class DuplicatedPhoneNumberException(Exception):
    def __init__(self, phone) -> None:
        super().__init__(f"Duplicated phone number {phone}")
