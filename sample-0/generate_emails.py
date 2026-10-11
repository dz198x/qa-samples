import random
import string


def random_local_part() -> str:
    """Левая часть: 1-8 символов, латиница и цифры."""
    alphabet = string.ascii_lowercase + string.digits
    length = random.randint(1, 8)
    return "".join(random.choices(alphabet, k=length))


def random_domain() -> str:
    """Домен: ровно 8 символов, латиница."""
    return "".join(random.choices(string.ascii_lowercase, k=8))


def random_tld() -> str:
    """TLD: ровно 3 символа, латиница (чтобы адрес был валидным)."""
    return "".join(random.choices(string.ascii_lowercase, k=3))


def random_email() -> str:
    local = random_local_part()
    domain = random_domain()
    tld = random_tld()
    return f"{local}@{domain}.{tld}"


def main() -> None:
    emails = [random_email() for _ in range(10)]
    for email in emails:
        print(email)


if __name__ == "__main__":
    main()
