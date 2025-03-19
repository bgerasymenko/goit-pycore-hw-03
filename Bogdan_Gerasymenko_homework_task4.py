from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Визначає найближчі дні народження колег на 7 днів вперед,
    включаючи перенесення привітань, якщо день народження випадає на вихідний.

    Параметри:
    - users (list): список словників із ключами 'name' і 'birthday' (формат 'рік.місяць.дата').

    Повертає:
    - list: список словників із іменами та датами привітань у форматі 'рік.місяць.дата'.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року, дивимось на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            # Перевіряємо, чи випадає день народження на вихідні
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays


# Приклад використання
if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.03.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
