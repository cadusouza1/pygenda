from exceptions import InvalidNameException, InvalidPhoneNumberException

PHONE_MAX_LEN = 13
PHONE_MIN_LEN = 9


def validade_contact_name(name: str):
    if name == "":
        raise InvalidNameException(name)


def validade_contact_phone(phone: str):
    if (
        not phone.isnumeric()
        or len(phone) > PHONE_MAX_LEN
        or len(phone) < PHONE_MIN_LEN
    ):
        raise InvalidPhoneNumberException(phone)
