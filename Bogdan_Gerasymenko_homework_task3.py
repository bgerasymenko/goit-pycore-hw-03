import re

def normalize_phone(phone_number):
    """
    Нормалізує номер телефону до стандартного формату для SMS-розсилок.

    Параметри:
    - phone_number (str): телефонний номер у будь-якому форматі.

    Повертає:
    - str: нормалізований номер телефону з міжнародним кодом '+38'.
    """
    # Видалення всіх зайвих символів крім цифр
    digits = re.sub(r'\D', '', phone_number)

    # Перевірка та додавання міжнародного коду
    if digits.startswith('380'):
        normalized = '+' + digits
    elif digits.startswith('0'):
        normalized = '+38' + digits
    else:
        normalized = '+380' + digits

    return normalized


# Приклад використання
if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
