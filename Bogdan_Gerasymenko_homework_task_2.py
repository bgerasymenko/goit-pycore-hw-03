from random import sample

def get_numbers_ticket(min, max, quantity):

    # Перевірка коректності вхідних параметрів
    if not (1 <= min < max <= 1000):
        raise ValueError("Неправильно задано межі діапазону (повинно бути від 1 до 1000 і min < max).")

    if quantity > (max - min + 1) or quantity <= 0:
        raise ValueError("Кількість чисел має бути більше 0 і не перевищувати розмір діапазону.")

    # Генерація унікальних чисел
    numbers = sample(range(min, max + 1), quantity)

    return sorted(numbers)


# Приклад використання
if __name__ == "__main__":
    try:
        ticket_numbers = get_numbers_ticket(1, 49, 6)
        print(f"Ваші числа для лотереї: {ticket_numbers}")
    except ValueError as e:
        print(e)
